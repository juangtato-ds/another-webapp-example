import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Observable, catchError, map, of } from 'rxjs';
import { ArtistMap, Song, SongForm, SongSummary } from './model/song.model';
import { SongResponse } from './model/song-api.model';
import { NonNullableFormBuilder, Validators } from '@angular/forms';

function mapSong(s: SongResponse): Song {
  return {
    id: s.id,
    title: s.title,
    artist: s.artist,
    lyrics: s.lyrics,
    countryList: s.country_list,
  };
}

function sortSongs(list: Array<SongSummary>): Array<SongSummary> {
  // TODO it is preferable to sort in the from, but this is for playing a little
  return list.sort((a, b) => a.title.localeCompare(b.title));
}

@Injectable({
  providedIn: 'root'
})
export class SongService {

  private readonly rootUrl = '/api/song/';

  constructor(
    private http: HttpClient,
    private nfb: NonNullableFormBuilder
  ) { }

  songSummaryList(): Observable<Array<SongSummary>> {
    return this.http.get<Array<SongSummary>>(this.rootUrl).pipe(map(sortSongs));
  }

  artistMap(): Observable<ArtistMap> {
    return this.songSummaryList().pipe(
      catchError(e => { // errors can be checked here
        alert("Couldn't retrieve song catalog");
        return of([]);
      }),
      map(songList => songList.reduce((acc, song) => {
        if (!acc[song.artist]) {
          acc[song.artist] = [];
        }
        acc[song.artist].push(song);
        return acc;
      }, {} as ArtistMap))
    )
  }

  get(songId: string): Observable<Song> {
    return this.http.get<SongResponse>(this.rootUrl + songId).pipe(
      map(mapSong)
    );
  }

  form(song?: SongForm) {
    return this.nfb.group({
      id: song?.id,
      artist: [song?.artist || '', Validators.required],
      title: [song?.title || '', Validators.required]
    });
  }

  create(song: SongForm): Observable<Song> {
    return this.http.post<SongResponse>(this.rootUrl, song).pipe(
      map(mapSong)
    );
  }
}

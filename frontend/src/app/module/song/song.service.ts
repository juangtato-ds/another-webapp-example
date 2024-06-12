import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Observable, map } from 'rxjs';
import { Song, SongForm, SongSummary } from './model/song.model';
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
    return this.http.get<Array<SongSummary>>(this.rootUrl);
  }

  get(songId: string): Observable<Song> {
    return this.http.get<SongResponse>(this.rootUrl + songId).pipe(
      map(mapSong)
    );
  }

  form(song?: Song) {
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

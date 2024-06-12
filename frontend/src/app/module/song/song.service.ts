import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Observable, map } from 'rxjs';
import { Song, SongSummary } from './model/song.model';
import { SongResponse } from './model/song-api.model';

@Injectable({
  providedIn: 'root'
})
export class SongService {

  constructor(
    private http: HttpClient
  ) { }

  songSummaryList(): Observable<Array<SongSummary>> {
    return this.http.get<Array<SongSummary>>('/api/song/');
  }

  get(songId: string): Observable<Song> {
    return this.http.get<SongResponse>(`/api/song/${songId}`).pipe(
      map(s => ({ // I don't want to work with snake_case or communication structure is not good for front
        id: s.id,
        title: s.title,
        artist: s.artist,
        lyrics: s.lyrics,
        countryList: s.country_list,
      }))
    );
  }
}

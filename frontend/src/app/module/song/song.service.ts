import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Observable } from 'rxjs';
import { SongSummary } from './model/song.model';

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
}

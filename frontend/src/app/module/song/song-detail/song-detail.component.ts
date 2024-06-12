import { ChangeDetectionStrategy, Component, OnInit, WritableSignal, inject, signal } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Song } from '../model/song.model';
import { SongService } from '../song.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-song-detail',
  standalone: true,
  imports: [
    CommonModule
  ],
  templateUrl: './song-detail.component.html',
  styleUrl: './song-detail.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SongDetailComponent implements OnInit {

  static readonly SONG_ID = "songId";

  private activatedRoute = inject(ActivatedRoute);
  private router = inject(Router);
  private songService = inject(SongService);
  private songId!: string;

  song: WritableSignal<Song | undefined> = signal(undefined);

  ngOnInit(): void {
    const songId = this.activatedRoute.snapshot.paramMap.get(SongDetailComponent.SONG_ID);
    if (!songId) {
      console.log('This should never happen, but in that case...');
      this.router.navigateByUrl('/');
    } else {
      this.songId = songId;
      this.loadSong();
    }
  }

  private loadSong(): void {
    this.songService.get(this.songId).subscribe({
      next: s=> this.song.set(s),
      error: e => this.processError(e)
    });
  }

  private processError(e: any): void {
    if (e.status == 404) {
      alert(`Song ${this.songId} not found!`);
    } else {
      alert(`Unexpected error ${e.status}, check later.`);
    }
    
    this.router.navigateByUrl('/');
  }



}

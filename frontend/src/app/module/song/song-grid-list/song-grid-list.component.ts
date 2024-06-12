import { ChangeDetectionStrategy, Component, OnInit, Signal, inject } from '@angular/core';
import { SongCardComponent } from '../song-card/song-card.component';
import { CommonModule } from '@angular/common';
import { FloatingButtonsComponent } from '../../../layout/floating-buttons/floating-buttons.component';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatTooltipModule } from '@angular/material/tooltip';
import { SongService } from '../song.service';
import { SongSummary } from '../model/song.model';
import { toSignal } from '@angular/core/rxjs-interop';
import { catchError, of } from 'rxjs';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { MatDialog } from '@angular/material/dialog';
import { SongFormDialogComponent } from '../song-form-dialog/song-form-dialog.component';

@Component({
  selector: 'app-song-grid-list',
  standalone: true,
  imports: [
    CommonModule,
    RouterLink,
    MatButtonModule,
    MatIconModule,
    MatTooltipModule,
    FloatingButtonsComponent,
    SongCardComponent,
  ],
  templateUrl: './song-grid-list.component.html',
  styleUrl: './song-grid-list.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SongGridListComponent {
  private songService = inject(SongService);
  private router = inject(Router);
  private activatedRouter = inject(ActivatedRoute);

  songList: Signal<Array<SongSummary>>

  constructor(
    private dialog: MatDialog
  ) {
    this.songList = toSignal(
      this.songService.songSummaryList()
        .pipe(
          catchError(e => {
            alert("Couldn't retrieve song catalog");
            return of([]);
          })
        ),
      { initialValue: [] }
    );
  }

  add(): void {
    const dialogRef = this.dialog.open(SongFormDialogComponent, { data: {} });
    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.songService.create(result).subscribe({
          next: s => this.router.navigate([s.id], { relativeTo: this.activatedRouter }),
          error: this.processError
        });
        // TODO loading animation
      }
    });
  }

  private processError(e: any): void {
    console.error(e);
    if (e.status == 400) {
      alert('Invalid request');
    } else if (e.status == 422) {
      alert('Song not found (or lyrics are missing)');
    } else {
      alert('Unexpected error');
    }
  }

}

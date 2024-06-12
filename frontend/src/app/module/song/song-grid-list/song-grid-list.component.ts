import { ChangeDetectionStrategy, Component, Signal } from '@angular/core';
import { SongCardComponent } from '../song-card/song-card.component';
import { CommonModule } from '@angular/common';
import { FloatingButtonsComponent } from '../../../layout/floating-buttons/floating-buttons.component';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatTooltipModule } from '@angular/material/tooltip';
import { SongSummary } from '../model/song.model';
import { toSignal } from '@angular/core/rxjs-interop';
import { catchError, of } from 'rxjs';
import { RouterLink } from '@angular/router';
import { AbstractAddSongComponent } from '../abstract-add-song.component';

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
export class SongGridListComponent extends AbstractAddSongComponent {

  songList: Signal<Array<SongSummary>>

  constructor() {
    super();
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

}

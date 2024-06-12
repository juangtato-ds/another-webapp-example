import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { RouterLink } from '@angular/router';
import { SongSummary } from '../model/song.model';
import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-song-card',
  standalone: true,
  imports: [
    RouterLink,
    MatCardModule,
  ],
  templateUrl: './song-card.component.html',
  styleUrl: './song-card.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SongCardComponent {
  @Input()
  song!: SongSummary;
}

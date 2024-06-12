import { ChangeDetectionStrategy, Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-song-card',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './song-card.component.html',
  styleUrl: './song-card.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SongCardComponent {

}

import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-song-detail',
  standalone: true,
  imports: [],
  templateUrl: './song-detail.component.html',
  styleUrl: './song-detail.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SongDetailComponent {

}

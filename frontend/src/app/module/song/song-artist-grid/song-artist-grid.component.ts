import { ChangeDetectionStrategy, Component, WritableSignal, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ArtistMap } from '../model/song.model';
import { FloatingButtonsComponent } from '../../../layout/floating-buttons/floating-buttons.component';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatTooltipModule } from '@angular/material/tooltip';
import { AbstractAddSongComponent } from '../abstract-add-song.component';

@Component({
  selector: 'app-song-artist-grid',
  standalone: true,
  imports: [
    RouterLink,
    MatButtonModule,
    MatIconModule,
    MatTooltipModule,
    FloatingButtonsComponent,
  ],
  templateUrl: './song-artist-grid.component.html',
  styleUrl: './song-artist-grid.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SongArtistGridComponent extends AbstractAddSongComponent {

  songMap: ArtistMap = {};
  artistList: WritableSignal<Array<string>> = signal([]);

  constructor() {
    super();
    this.songService.artistMap().subscribe(a => {
      this.songMap = a;
      this.artistList.set(Object.keys(a));
    });
  }

}

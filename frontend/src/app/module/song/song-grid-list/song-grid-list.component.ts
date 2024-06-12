import { ChangeDetectionStrategy, Component } from '@angular/core';
import { SongCardComponent } from '../song-card/song-card.component';
import { CommonModule } from '@angular/common';
import { FloatingButtonsComponent } from '../../../layout/floating-buttons/floating-buttons.component';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatTooltipModule } from '@angular/material/tooltip';

@Component({
  selector: 'app-song-grid-list',
  standalone: true,
  imports: [
    CommonModule,
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

}

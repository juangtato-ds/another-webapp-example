import { ChangeDetectionStrategy, Component, Inject } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { MAT_DIALOG_DATA, MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { SongFormDialogData } from './song-form-dialog-data';
import { SongService } from '../song.service';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { SongForm } from '../model/song.model';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-song-form-dialog',
  standalone: true,
  imports: [
    ReactiveFormsModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatDialogModule,
  ],
  templateUrl: './song-form-dialog.component.html',
  styleUrl: './song-form-dialog.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SongFormDialogComponent {

  form = this.songService.form(this.data.song);

  constructor(
    private songService: SongService,
    private dialogRef: MatDialogRef<SongFormDialogComponent, SongForm>,
    @Inject(MAT_DIALOG_DATA) public data: SongFormDialogData,
  ) { }

  save(): void {
    if (this.form.valid) {
      this.dialogRef.close(this.form.getRawValue());
    } else {
      this.form.markAllAsTouched();
    }
  }

  cancel(): void {
    this.dialogRef.close();
  }
}

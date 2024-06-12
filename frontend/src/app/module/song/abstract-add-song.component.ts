import { inject } from "@angular/core";
import { MatDialog } from "@angular/material/dialog";
import { ActivatedRoute, Router } from "@angular/router";
import { SongService } from "./song.service";
import { SongFormDialogComponent } from "./song-form-dialog/song-form-dialog.component";

export abstract class AbstractAddSongComponent {
    protected songService = inject(SongService);
    protected router = inject(Router);
    protected activatedRouter = inject(ActivatedRoute);
    protected dialog = inject(MatDialog);

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
import { Routes } from '@angular/router';
import { WelcomeComponent } from './module/landing/welcome/welcome.component';
import { ParentComponent } from './layout/parent/parent.component';
import { SongGridListComponent } from './module/song/song-grid-list/song-grid-list.component';
import { SongDetailComponent } from './module/song/song-detail/song-detail.component';

export const routes: Routes = [
    {
        path: '',
        component: WelcomeComponent,
        pathMatch: 'full'
    },
    {
        path: 'song',
        component: ParentComponent,
        children: [
            {
                path: '',
                component: SongGridListComponent
            },
            {
                path: ':' + SongDetailComponent.SONG_ID,
                component: SongDetailComponent
            }
        ]
    }
];

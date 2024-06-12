import { Route, Routes } from "@angular/router";
import { ParentComponent } from "../../layout/parent/parent.component";
import { SongGridListComponent } from "./song-grid-list/song-grid-list.component";
import { SongDetailComponent } from "./song-detail/song-detail.component";
import { SongArtistGridComponent } from "./song-artist-grid/song-artist-grid.component";

const songRoute: Route = {
    path: ':' + SongDetailComponent.SONG_ID,
    component: SongDetailComponent

};

export const songRoutes: Routes = [
    {
        path: 'song',
        component: ParentComponent,
        children: [
            {
                path: '',
                component: SongGridListComponent
            },
            songRoute
        ]
    },
    {
        path: 'artist-song',
        component: ParentComponent,
        children: [
            {
                path: '',
                component: SongArtistGridComponent
            },
            songRoute
        ]
    }
];
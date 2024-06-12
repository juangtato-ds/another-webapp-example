import { Routes } from '@angular/router';
import { WelcomeComponent } from './module/landing/welcome/welcome.component';
import { songRoutes } from './module/song/song.routes';


export const routes: Routes = [
    {
        path: '',
        component: WelcomeComponent,
        pathMatch: 'full'
    },
    ...songRoutes

];

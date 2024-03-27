import { Routes } from '@angular/router';
import { MainComponent } from './views/main/main.component';
import { LoginComponent } from './views/login/login.component';
import { HomeComponent } from './views/main/home/home.component';
import { CurrentComponent } from './views/main/current/current.component';
import { CollectionComponent } from './views/main/collection/collection.component';
import { StatsComponent } from './views/main/stats/stats.component';
import { SettingsComponent } from './views/main/settings/settings.component';

export const routes: Routes = [
    {
        path: '',
        component: MainComponent,
        children: [
            {
                path: 'home',
                component: HomeComponent
            },
            {
                path: 'current',
                component: CurrentComponent
            },
            {
                path: 'collection',
                component: CollectionComponent
            },
            {
                path: 'stats',
                component: StatsComponent
            },
            {
                path: 'settings',
                component: SettingsComponent
            }
        ],
        canActivate: [() => true]
    },
    {
        path: 'login',
        component: LoginComponent,
    },
    {
        path: '**',
        redirectTo: ''
    }
];



// Routing::get('signup', 'SecurityController');
// Routing::get('login', 'SecurityController');
// Routing::get('logout', 'SecurityController');
// Routing::get('delete_user_by_id', 'SecurityController');
// Routing::get('delete_user', 'SecurityController');

// Routing::get('add_session', 'SessionController');

// Routing::get('add_book', 'BookController');
// Routing::get('delete_book', 'BookController');

// Routing::get('start_screen', 'DefaultController');
// Routing::get('book_details', 'DefaultController');
// Routing::get('collection', 'DefaultController');
// Routing::get('current_book', 'DefaultController');
// Routing::get('dashboard', 'DefaultController');
// Routing::get('reading_session', 'DefaultController');
// Routing::get('end_reading_session', 'DefaultController');
// Routing::get('stats', 'DefaultController');
// Routing::get('settings', 'DefaultController');
// Routing::get('settings_admin', 'DefaultController');
// Routing::get('search', 'DefaultController');
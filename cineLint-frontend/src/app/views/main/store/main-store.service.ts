import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

export type SubpageType = 'Home' | 'Current' | 'Collection' | 'Stats' | 'Settings'

@Injectable({
  providedIn: 'root'
})
export class MainStoreService {
  private currentSubpage = new Subject<SubpageType>();

  currentSubpage$ = this.currentSubpage.asObservable();

  setCurrentSubpage(subpage: SubpageType) {
    this.currentSubpage.next(subpage);
  }

}

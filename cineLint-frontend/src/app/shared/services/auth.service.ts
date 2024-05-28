import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  userId = 2;
  
  get token() {
    return "4af411a51c959421ebafd88cc12dd76cfcf2881d"
  }

  constructor() { }

  logout() {

  }

  deleteAccount() {
    
  }
}

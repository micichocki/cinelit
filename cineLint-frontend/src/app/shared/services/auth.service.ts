import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable, catchError, map, of } from "rxjs";

@Injectable({
  providedIn: "root",
})
export class AuthService {
  private readonly API_URL = "https://localhost:8080/api/auth";

  userId = 2;

  get token() {
    return "390bb871f7bd42a97933f8edd40cea0e8845c471";
  }

  constructor(private http: HttpClient) {}

  login(credentials: { email: string; password: string }): Observable<any> {
    return this.http.post<any>(`${this.API_URL}/login`, credentials).pipe(
      map((response) => {
        localStorage.setItem("user", JSON.stringify(response.user));
        localStorage.setItem("token", response.token);
        return response;
      }),
      catchError(this.handleError("login", []))
    );
  }

  logout(): void {
    localStorage.removeItem("user");
    localStorage.removeItem("token");
  }

  deleteAccount(): Observable<any> {
    const user = this.getUser();
    if (!user) {
      return of(null);
    }
    return this.http.delete<any>(`${this.API_URL}/users/${user.id}`).pipe(
      map((response) => {
        this.logout();
        return response;
      }),
      catchError(this.handleError("deleteAccount", []))
    );
  }

  getUser(): any {
    const user = localStorage.getItem("user");
    return user ? JSON.parse(user) : null;
  }

  private handleError<T>(operation = "operation", result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }
}

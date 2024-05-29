import { HttpBackend, HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, map, of, switchMap } from 'rxjs';
import { APIMovie } from '../models/movies';

export interface CollectionResponse {
  books: Book[]
  films: Movie[]
}

interface Author {
  first_name: string;
  last_name: string;
}

interface Genre {
  genre_name: string;
}

export interface Book {
  id?: number;
  title: string;
  released: string; // Use Date if you prefer working with Date objects
  genre: Genre;
  authors: Author[];
  num_of_pages: number;
  plot?: string;
  cover: string
}

export interface Movie {
  id?: number;
  title: string;
  released: string; // Use Date if you prefer working with Date objects
  genre: Genre;
  directors: Author[];
  length: number;
  plot?: string;
  cover: string
}

export interface Session {
  id?: number,
  item_id: number,
  start_date: string
  end_date: string,
  duration?: number,
  pages_read?: number,
  watching_time?: number
}

@Injectable({
  providedIn: 'root'
})
export class RepositoryService {
  API_URL = 'http://localhost:8000/api'
  API_KEY = "b9285cf3"

  constructor(private http: HttpClient, private httpBackend: HttpBackend) { }

  addMovie(movie: any): any {
    return this.http.post(this.API_URL + '/films/', movie)
  }

  addBook(book: Book): any {
    return this.http.post(this.API_URL + '/books/', book)
  }

  getObjectById(userId: number, id: number): Observable<Book | Movie> {
    return this.http.get<Book | Movie>(this.API_URL + '/books/' + id)
      .pipe(
        catchError(err => this.http.get(this.API_URL + '/films/' + id).pipe(
          map((res: any) => { return { ...res, cover: res.poster } as Movie })
        ))
      )
  }

  getCollectionByUserId(userId: number): Observable<CollectionResponse> {
    return this.http.get<CollectionResponse>(this.API_URL + '/users/'+userId+'/collections').pipe(map((res) => {
      if (res.films) {
        res.films = res.films.map((film: any) => {
          return {
            ...film,
            cover: film.poster
          }
        })
      }
      return res;
    }));
    // return of(collectionResponse)
  }

  saveSession(userId: number, session: Session): Observable<any> {
    return this.http.post(this.API_URL + '/users/' + userId + '/sessions/', session)
  }

  searchMovieByTitle(title: string): Observable<APIMovie> {
    const httpClient = new HttpClient(this.httpBackend);

    const titleParts = title.trim().split(' ');
    return httpClient.get<APIMovie>(`http://www.omdbapi.com/?apikey=${this.API_KEY}&t=` + titleParts.join("+"));
  }
  searchBookByTitle(title: string) {
    const book = collectionResponse.books
    .find(book => book.title.toLocaleLowerCase().includes(title.toLowerCase()))
    
    return of({ ...book, genre: book?.genre.join(', ') });
    // return this.http.get("" + title);
  }
}

const collectionResponse = {
  books: [
    {
      id: 1,
      title: 'The shining',
      url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMgjXdFvQYm5rrNfmo4PD4ux4d4i_KewKrvadL4ixwtA&s',
      author: 'Stephen King',
      pages: 150,
      genre: ['Drama', 'Fiction'],
      objectType: 'Book'
    },
    {
      id: 2,
      title: 'The shining',
      url: 'https://www.mediarodzina.pl/mrcore/uploads/2018/11/lew_czarownica_i_stara_szafa_okladka_filmowa-1.jpg',
      author: 'Stephen King',
      pages: 150,
      genre: ['Drama', 'Fiction'],
      objectType: 'Book'
    },
    {
      id: 3,
      title: 'The shining',
      url: 'https://m.media-amazon.com/images/I/71jDX01PzaL._AC_UF894,1000_QL80_.jpg',
      author: 'Stephen King',
      pages: 150,
      genre: ['Drama', 'Fiction'],
      objectType: 'Book'
    },
    {
      id: 5,
      title: 'The shining',
      url: 'https://m.media-amazon.com/images/I/81nq+ewtkcL._AC_UF894,1000_QL80_.jpg',
      author: 'Stephen King',
      pages: 150,
      genre: ['Drama', 'Fiction'],
      objectType: 'Book'
    },
    {
      id: 4,
      title: 'The shining',
      url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMgjXdFvQYm5rrNfmo4PD4ux4d4i_KewKrvadL4ixwtA&s',
      author: 'Stephen King',
      pages: 150,
      genre: ['Drama', 'Fiction'],
      objectType: 'Book'
    },
    {
      id: 6,
      title: 'The shining',
      url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMgjXdFvQYm5rrNfmo4PD4ux4d4i_KewKrvadL4ixwtA&s',
      author: 'Stephen King',
      pages: 150,
      genre: ['Drama', 'Fiction'],
      objectType: 'Book'
    },
    {
      id: 7,
      title: 'The shining',
      url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMgjXdFvQYm5rrNfmo4PD4ux4d4i_KewKrvadL4ixwtA&s',
      author: 'Stephen King',
      pages: 150,
      genre: ['Drama', 'Fiction'],
      objectType: 'Book'
    }
  ],
  movies: [
    {
      id: 2,
      title: 'Star Wars: The Empire strikes back',
      url: 'https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
      director: 'Irvin Kershner',
      objectType: 'Movie'
    },
    {
      id: 3,
      title: 'Star Wars: The Empire strikes back',
      url: 'https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
      director: 'Irvin Kershner',
      objectType: 'Movie'
    },
    {
      id: 4,
      title: 'Star Wars: The Empire strikes back',
      url: 'https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
      director: 'Irvin Kershner',
      objectType: 'Movie'
    },
    {
      id: 5,
      title: 'Star Wars: The Empire strikes back',
      url: 'https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
      director: 'Irvin Kershner',
      objectType: 'Movie'
    },
    {
      id: 6,
      title: 'Star Wars: The Empire strikes back',
      url: 'https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
      director: 'Irvin Kershner',
      objectType: 'Movie'
    },
    {
      id: 7,
      title: 'The shining',
      url: 'https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg',
      director: 'Irvin Kershner',
      objectType: 'Movie'
    }
  ]
}

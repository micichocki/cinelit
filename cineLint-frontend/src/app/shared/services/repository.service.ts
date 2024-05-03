import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

export interface CollectionResponse {
  books: any[]
  movies: any[]
}

@Injectable({
  providedIn: 'root'
})
export class RepositoryService {
  API_URL = 'https://localhost:8080/api'
  API_KEY = "1231"

  constructor(private http: HttpClient) { }

  getAllMovies(): Observable<any> {
    return this.http.get(this.API_URL + '/movies');
  }

  getAllBooks(): Observable<any> {
    return this.http.get(this.API_URL + '/books');
  }

  addMovie(movie: any): any {
    this.http.post(this.API_URL + '/movie/add', movie)
  }

  addBook(book: any): any {
    this.http.post(this.API_URL + '/book/add', book)
  }

  getObjectById(id: number): Observable<any> {
    // return this.http.get(this.API_URL + '/repository/' + id);
    return of(collectionResponse.books[id]);
  }

  getCollectionByUserId(userId: number): Observable<CollectionResponse> {
    // return this.http.get<CollectionResponse>(this.API_URL + '/collection'),;
    return of(collectionResponse)
  }

  saveSession(session: any): Observable<any> {
    return this.http.post(this.API_URL + '/session/add', session)
  }

  searchMovieByTitle(title: string) {
    const movie = collectionResponse.movies
    .find(movie => movie.title.toLocaleLowerCase().includes(title.toLowerCase()))
    
    return of(movie);
    // const titleParts = title.trim().split(' ');
    // return this.http.get(`http://www.omdbapi.com/?apikey=${this.API_KEY}&t=` + titleParts.join("+"));
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

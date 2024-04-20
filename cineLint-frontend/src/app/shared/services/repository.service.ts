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
  API_URL = 'https://localhost:8080/ap,i'

  constructor(private http: HttpClient) { }

  getAllMovies(): Observable<any> {
    return this.http.get(this.API_URL + '/movies');
  }

  getAllBooks(): Observable<any> {
    return this.http.get(this.API_URL + '/books');
  }

  getCollectionByUserId(userId: number): Observable<CollectionResponse> {
    // return this.http.get<CollectionResponse>(this.API_URL + '/collection'),;
    return of(collectionResponse)
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
      url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMgjXdFvQYm5rrNfmo4PD4ux4d4i_KewKrvadL4ixwtA&s',
      author: 'Stephen King',
      pages: 150,
      genre: ['Drama', 'Fiction'],
      objectType: 'Book'
    },
    {
      id: 3,
      title: 'The shining',
      url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMgjXdFvQYm5rrNfmo4PD4ux4d4i_KewKrvadL4ixwtA&s',
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
      id: 5,
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

import axios from 'axios';
import Moment from 'moment'
import React, {Component} from 'react';

import Page404 from './../404/Page404'
import './Movies.sass';

const DefaultThumb = require('../../img/default-thumb.png')


export default class Header extends Component {
  state = {
    movies: [],
  }

  componentDidMount() {
    axios.get('http://localhost:8000/api/movies/')
      .then((res) => {
        console.log(res.data)
        const movies = res.data;
        this.setState({ movies })
      })
      .catch((e) => {
        console.log(e) // if error status code...
      })
  }

  render () {
    const col_style = {
      'padding': '0 12px',
    };
    const movies_list = this.state.movies.map((movie) => {
      const moviepanel_url = `/${movie.moviepanel.slug}/`;
      const movie_url = `/${movie.moviepanel.slug}/${movie.id}/`;
      const moviegenre_slice = movie.moviegenre.slice(0, 4);
      const moviegenres = moviegenre_slice.map((moviegenre) => {
        const moviegenre_url = `/${moviegenre.moviepanel.slug}/${moviegenre.slug}/`;
        return (
          <a className="card-body__moviegenres--moviegenre" href={moviegenre_url} key={moviegenre.id}>
            <span>{moviegenre.name}</span>
          </a>
        );
      });

      return (
        <div className="col-md-3" style={col_style} key={movie.id}>
          <div className="card" href={movie_url}> {/* Todo card <a> */}
            <a className="card__moviepanel" href={moviepanel_url}>
              <span>{movie.moviepanel.name}</span>
            </a>
            <img className="card-img-top" src={movie.poster_url ? movie.poster_url : DefaultThumb} alt={movie.name} />
            <div className="card-body">
              <div className="card-body__moviegenres">
                {moviegenres}
              </div>
              <h5 className="card-title">{movie.name}</h5>
              <p className="card-text">{movie.description}</p>
            </div>
            <div className="card-footer">
              <small className="text-muted float-left">Published at: </small>
              <small className="text-muted float-right">
                {Moment(movie.published_at).format('d MMM HH:mm')}
              </small>
              {/*<small className="text-muted">Updated at {movie.modified}</small>*/}
            </div>
          </div>
        </div>
      );
    })

    return (
      <div className="container">
        <div className="row">
          <div className="card-deck">
            {movies_list}
          </div>
        </div>
      </div>
    );
  }
}

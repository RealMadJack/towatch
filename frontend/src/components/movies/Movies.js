import axios from 'axios';
import React, {Component} from 'react';

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
        const movies = res.data
        this.setState({ movies })
      })
      .catch((e) => {
        console.log(e)
      })
  }

  render () {
    const movies_list = this.state.movies.map((movie) => {
      const col_style = {
        'padding': '0 12px',
      }
      const moviegenre_slice = movie.moviegenre.slice(0, 4)
      return (
        <div className="col-md-3" style={col_style} key={movie.id}>
          <div className="card">
              <a className="card__moviepanel" href="#">
                <span>{movie.moviepanel.name}</span>
              </a>
              <img className="card-img-top" src={movie.poster_url ? movie.poster_url : DefaultThumb} alt={movie.name} />
            <div className="card-body">
              <div className="card-body__moviegenres">
                {moviegenre_slice.map((genre) => <a className="card-body__moviegenres--moviegenre" href="#" key={genre.id}><span>{genre.name}</span></a>)}
              </div>
              <h5 className="card-title">{movie.name}</h5>
              <p className="card-text">{movie.description}</p>
            </div>
            <div className="card-footer">
              <small className="text-muted">Published at {movie.published_at}</small>
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

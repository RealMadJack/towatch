import axios from 'axios';
import React, {Component} from 'react';

import './Movies.sass';

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
      return (
        <div className="col-md-3">
          <div className="card">
            <img className="card-img-top" src="" alt="Card image cap" />
            <div className="card-body">
              <h5 className="card-title">{movie.name}</h5>
              <p className="card-text">{movie.description}</p>
            </div>
            <div className="card-footer">
              <small className="text-muted">Published at {movie.published_at}</small>
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

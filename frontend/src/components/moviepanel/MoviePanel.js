import axios from 'axios';
import Moment from 'moment';
import React, {Component} from 'react';

import './MoviePanel.sass';

const DefaultThumb = require('../../img/default-thumb.png')


export default class MoviePanel extends Component {
  state = {
    moviepanel: {
      movies: [],
      moviegenres: [],
    },
  }

  componentDidMount() {
    const request = this.props.match.params;
    axios.get(`http://localhost:8000/api/panels/${request.moviepanel}`)
      .then((res) => {
        console.log(res.data)
        const moviepanel = res.data
        this.setState({ moviepanel });
      })
      .catch((e) => {
        console.log(e)
      })
  }

  render() {
    const col_style = {
      'padding': '0 12px',
    };
    const moviepanel = this.state.moviepanel
    const moviepanel_movies = moviepanel.movies.map((movie) => {
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

      return(
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
            {moviepanel_movies}
          </div>
        </div>
      </div>
    );
  }
}

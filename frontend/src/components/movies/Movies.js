import axios from 'axios';
import Moment from 'moment'
import React, {Component} from 'react';

import Preloader from './../preloader/Preloader';
import Page404 from './../404/Page404';
import './Movies.sass';

const DefaultThumb = require('../../img/default-thumb.png');
const timeout = 100;


export default class Header extends Component {
  state = {
    movies: [],
    error: {
      msg: '',
      status: null,
    }
  }

  componentDidMount() {
    setTimeout(() => {
      axios.get('http://localhost:8000/api/movies/')
        .then((res) => {
          console.log(res.data);
          const movies = res.data;
          this.setState({
            movies: movies,
            error: {
              status: 200,
            }
          });
        })
        .catch((e) => {
          if (e.response) {
            this.setState({
              error: {
                msg: e,
                status: e.response.status
              }
            });
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            // console.log(error.response.data);
            // console.log(error.response.status);
            // console.log(error.response.headers);
          } else if (e.request) {
            // The request was made but no response was received
            // `error.request` is an instance of XMLHttpRequest in the
            // browser and an instance of
            // http.ClientRequest in node.js
            console.log(e.request);
          } else {
            // Something happened in setting up the request that triggered an Error
            console.log('Error', e.message);
          }
          console.log(e.config);

        })
    }, timeout)
  }

  render () {
    if (this.state.error.status === 404) {
      return(
        <Page404 />
      )
    }

    const col_style = {
      'padding': '0 12px',
    };
    const movies_list = this.state.movies.map((movie) => {
      const moviepanel_url = `/${movie.moviepanel.slug}/`;
      const movie_url = `/${movie.moviepanel.slug}/${movie.id}/`;
      const moviegenre_slice = movie.moviegenre.slice(0, 4);
      const moviegenres = moviegenre_slice.map((moviegenre) => {
        const moviegenre_url = `/category/${moviegenre.slug}/`;
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

    if (this.state.error.status === 200) {
      return (
        <div className="container">
          <div className="row">
            <div className="card-deck">
              {movies_list}
            </div>
          </div>
        </div>
      );
    } else {
      return(
        <Preloader />
      );
    }

  }
}

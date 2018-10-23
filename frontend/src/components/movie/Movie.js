import axios from 'axios';
import React, {Component} from 'react';
import Moment from 'moment';

import Page404 from './../404/Page404';
import Preloader from './../preloader/Preloader';
import './Movie.sass';

const DefaultThumb = require('../../img/default-thumb.png');
const timeout = 100;


export default class Movie extends Component {
  state = {
    movie: {
      moviepanel: {},
      moviegenres: [],
    },
    error: {
      msg: '',
      status: null,
    }
  }

  componentDidMount() {
    const request = this.props.match.params;
    setTimeout(() => {
      axios.get(`http://localhost:8000/api/movies/${request.movie}`)
        .then((res) => {
          console.log(res.data);
          const movie = res.data;
          if (movie.moviepanel.slug === request.moviepanel) {
            this.setState({
              movie: movie,
              error: {
                status: 200,
              }
            });
          } else {
            this.setState({
              error: {
                status: 404,
              }
            });
          }
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

  render() {
    if (this.state.error.status === 404) {
      return(
        <Page404 />
      )
    }

    if (this.state.error.status === 200) {
      const movie = this.state.movie;
      const moviegenres = movie.moviegenre.map((moviegenre) => {
        const moviegenre_url = `/category/${moviegenre.slug}/`;
        return(
          <a className="moviegenre" href={moviegenre_url} key={moviegenre.id}>
            <span>{moviegenre.name}</span>
          </a>
        );
      })

      return (
        <div className="container">
          <div className="row">
            <div className="movie">
              <div className="movie__title">
                <div className="movie__title--name"><h1>{movie.name}</h1></div>
                <div className="movie__title--rank"><span>*****</span></div>
              </div>
              <div className="movie__description">
                <div className="movie__description--poster">
                  <img src={movie.poster_url ? movie.poster_url : DefaultThumb} alt={movie.name} />
                </div>
                <div className="movie__description--info">
                  <p className="plot">{movie.description}</p>
                  <p>Duration: {movie.duration}</p>
                  <p>Country: {movie.country}</p>
                  <p>Genres: {moviegenres}</p>
                  <p>Producer: </p>
                  <p>Actors: </p>
                  <p>Release date: {movie.release_date}</p>
                  <p>Last update: {Moment(movie.modified).format('D MMM HH:mm')}</p>
                </div>
              </div>
              <div className="movie__video-player">
                <nav>
                  <div className="nav nav-tabs" id="nav-tab" role="tablist">
                    <a className="nav-item nav-link active" id="nav-home-tab" data-toggle="tab" href="#nav-home">
                      Home
                    </a>
                    <a className="nav-item nav-link" id="nav-profile-tab" data-toggle="tab" href="#nav-profile">Profile
                    </a>
                    <a className="nav-item nav-link" id="nav-trailer-tab" data-toggle="tab" href="#nav-trailer">
                      Trailer
                    </a>
                  </div>
                </nav>
                <div className="tab-content" id="nav-tabContent">
                  <div className="tab-pane fade show active" id="nav-home" role="tabpanel">
                    Content of 1
                  </div>
                  <div className="tab-pane fade" id="nav-profile" role="tabpanel">
                    Content of 2
                  </div>
                  <div className="tab-pane fade" id="nav-trailer" role="tabpanel">
                    Content of 3
                    {/*<iframe width="560" height="315" src={movie.trailer ? movie.trailer : ''} frameBorder="0" allow="encrypted-media" allowFullScreen></iframe>*/}
                  </div>
                </div>
              </div>
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

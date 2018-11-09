import axios from 'axios';
import React, {Component} from 'react';
import update from 'react-addons-update';
import Moment from 'moment';
import YouTube from 'react-youtube';

import Page404 from './../404/Page404';
import Preloader from './../preloader/Preloader';
import './Movie.sass';

const DefaultThumb = require('../../img/default-thumb.png');
const RatingStar = require('../../img/rating-star.png');
const timeout = 100;


export default class Movie extends Component {
  constructor(props) {
    super(props);
    this.youtubePlayerAnchor = '1cH2cerUpMQ';
    this.state = {
      movie: {
        moviepanel: {},
        moviegenres: [],
      },
      error: {
        msg: '',
        status: null,
      },
      yt_player: [],
    }
  };

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

  _onReady(e) {
    this.setState(prevState => ({
      yt_player: [
        ...prevState.yt_player,
        {
          player: e,
          player_ready: true,
          playing: false,
          errors: [],
        }
      ]
    }));
    this.state.yt_player.map((yt_player) => {
      yt_player.player.target.pauseVideo();
      return false
    });
  }

  _onPlay(e) {
    const target = e.target
    this.state.yt_player.map((yt_player, index) => {
      if (target === yt_player.player.target) {
        this.setState({
          yt_player: update(
            this.state.yt_player, {[index]: {
              playing: {$set: true}
            }}
          )
        });
      }
      return false
    });
  }

  _onPause(e) {
    const target = e.target
    this.state.yt_player.map((yt_player, index) => {
      if (target === yt_player.player.target) {
        this.setState({
          yt_player: update(
            this.state.yt_player, {[index]: {
              playing: {$set: false}
            }}
          )
        });
      }
      return false
    });
  }

  onTabChange(e) {
    // if (e.target.id === 'nav-trailer-tab') {
    //   this.state.player_ready ? this.state.player.target.playVideo() : setTimeout(() => {
    //     this.state.player.target.playVideo()
    //   }, 1000)
    // }
    if (e.target.id !== 'nav-trailer-tab') {
      this.state.yt_player.map((yt_player, index) => {
        if (yt_player.playing === true) {
          yt_player.player.target.pauseVideo();
        }
        return false
      });
    }
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
          <a className="movie-genre" href={moviegenre_url} key={moviegenre.id}>
            <span>{moviegenre.name}</span>
          </a>
        );
      })
      const movieactors = movie.actors.map((actor, index) => {
        return(
          <span className="movie-actor" key={index}>{actor}</span>
        );
      })
      const yt_opts = {
        // height: '390',
        // width: '640',
        playerVars: { // https://developers.google.com/youtube/player_parameters
          autoplay: 0
        }
      };
      const yt_trailers = movie.yt_trailer_id.slice(0, 2).map((yt_id, index) => {
        const player_id = "player" + index
        return(
          <YouTube
            videoId={yt_id}
            className="yt_player"
            id={player_id}
            ref={player_id}
            opts={yt_opts}
            onReady={this._onReady.bind(this)}
            onPlay={this._onPlay.bind(this)}
            onPause={this._onPause.bind(this)}
            key={index}
          />
        );
      })

      return (
        <div className="container">
          <div className="row">
            <div className="movie">
              <div className="movie__title">
                <div className="movie__title--name"><h1>{movie.name}</h1></div>
                <div className="movie__title--rating">
                  <span>IMDB</span>
                  <img className="rating-star" src={RatingStar} alt="rating" />
                  <span className="rating-string">{movie.rating} / 10</span>
                </div>
              </div>
              <div className="movie__description">
                <div className="movie__description--poster">
                  <img src={movie.poster_url ? movie.poster_url : DefaultThumb} alt={movie.name} />
                </div>
                <div className="movie__description--info">
                  <p className="plot">{movie.description}</p>
                  <p>Duration: {movie.duration}min</p>
                  <p>Country: {movie.country}</p>
                  <p>Genres: {moviegenres}</p>
                  <p>Actors: {movieactors}</p>
                  <p>Seasons: {movie.seasons}</p>
                  <p>Language: {movie.original_language[0]}</p>
                  <p>Release date: {movie.release_date}</p>
                  <p>Last update: {Moment(movie.modified).format('D MMM HH:mm')}</p>
                </div>
              </div>
              <div className="movie__video-player">
                <nav>
                  <div className="nav nav-tabs" id="nav-tab" role="tablist" onClick={this.onTabChange.bind(this)}>
                    <a className="nav-item nav-link" id="nav-home-tab" data-toggle="tab" href="#nav-home">
                      Home
                    </a>
                    <a className="nav-item nav-link" id="nav-profile-tab" data-toggle="tab" href="#nav-profile">Profile
                    </a>
                    <a className="nav-item nav-link active" id="nav-trailer-tab" data-toggle="tab" href="#nav-trailer">
                      Trailer
                    </a>
                  </div>
                </nav>
                <div className="tab-content" id="nav-tabContent">
                  <div className="tab-pane fade" id="nav-home" role="tabpanel">
                    Content of 1
                  </div>
                  <div className="tab-pane fade" id="nav-profile" role="tabpanel">
                    Content of 2
                  </div>
                  <div className="tab-pane fade show active" id="nav-trailer" role="tabpanel">
                    {yt_trailers}
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

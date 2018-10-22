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
    return(
      <div>movie is working</div>
    );
  }
}

import axios from 'axios';
import Moment from 'moment';
import React, {Component} from 'react';

import Page404 from './../404/Page404'
import Preloader from './../preloader/Preloader'
import './MovieGenre.sass';

const DefaultThumb = require('../../img/default-thumb.png')

export default class MovieGenre extends Component {
  state = {
    moviegenre: {
      movies: [],
      moviepanel: {},
    },
    error: {
      msg: '',
      status: null,
    }
  }

  componentDidMount() {
    const request = this.props.match.params;
    axios.get(`http://localhost:8000/api/genres/${request.moviegenre}`)
      .then((res) => {
        console.log(res.data);
        const moviegenre = res.data;

        if (moviegenre.moviepanel.slug === request.moviepanel) {
          this.setState({
            moviegenre: moviegenre,
            error: {
              status: 200
            },
          });
        } else {
          this.setState({
            error: {
              msg: 'Incorrect moviepanel',
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
  }

  render() {
    // check if not status
    if (this.state.error.status === 404) {
      return(
        <Page404 />
      )
    } else if (this.state.error.status === 200) {
      return(
        <div>
          genre is working
        </div>
      );
    } else {
      return(
        <Preloader />
      );
    }

  }
}

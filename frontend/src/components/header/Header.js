import axios from 'axios';
import React, {Component} from 'react';

import Page404 from './../404/Page404';
import './Header.sass';


export default class Header extends Component {
  state = {
    moviepanels: [],
    error: {
      msg: '',
      status: null,
    }
  }

  componentDidMount() {
    axios.get('http://localhost:8000/api/panels/')
      .then(res => {
        console.log(res.data);
        const moviepanels = res.data;
        this.setState({ moviepanels });
        /* timeout */
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
    if (this.state.error.status === 404) {
      return(
        <Page404 />
      )
    }

    const moviepanels_list = this.state.moviepanels.map((moviepanel) => {
      const moviepanel_url = `/${moviepanel.slug}/`;
      const moviegenres = moviepanel.moviegenres.map((moviegenre) => {
        const moviegenre_url = `/category/${moviegenre.slug}/`;
        return(
          <a className="dropdown-item" href={moviegenre_url} key={moviegenre.id}>
            {moviegenre.name}
          </a>
        );
      })
      return (
        <li className="nav-item dropdown" key={moviepanel.id}>
          <a className="nav-link dropdown-toggle" href={moviepanel_url} id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            {moviepanel.name}
          </a>
          <div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            {moviegenres}
          </div>
        </li>
      );
    })

    return (
      <header className="main-header">
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <a className="navbar-brand" href="/">ToWatch</a>
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNavDropdown">
            <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
              <li className="nav-item active">
                <a className="nav-link" href="/">Home <span className="sr-only">(current)</span></a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/">Features</a>
              </li>
              {moviepanels_list}
            </ul>
            <ul class="navbar-nav my-2 my-lg-0">
              <li className="nav-item">
                <a className="nav-link" href="/signin">Sign In</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/signup">Sign Up</a>
              </li>
            </ul>
          </div>
        </nav>
      </header>
    );
  }
}

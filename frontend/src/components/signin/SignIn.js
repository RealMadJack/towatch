import axios from 'axios';
import React, {Component} from 'react';

import CSRFToken, {csrftoken_str} from './../csrf/csrftoken';
import Page404 from './../404/Page404';
import './SignIn.sass';


export default class SignIn extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      password: '',
      error: {
        msg: '',
        status: null,
      },
      endpoint: 'http://localhost:8000/api/token/',
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  };

  handleChange = e => {
    this.setState({
        [e.target.name]: e.target.value,
    });
  };

  handleSubmit = e => {
    e.preventDefault();
    console.log(this.state);
    const user = {
      name: this.state.name,
      password: this.state.password,
    }

    // axios.defaults.xsrfCookieName = 'csrftoken';
    // axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    // axios.defaults.headers.common['HTTP_X_CSRFTOKEN'] = csrftoken_str;
    axios.post(this.state.endpoint, {username: user.name, password: user.password})
      .then((res) => {
        console.log(res)
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
  };

  render() {
    return(
      <div className="container">
        <div className="row">
          <h1 className="col-12">Sign In:</h1>
          <form className="sign-form" onSubmit={this.handleSubmit}>
            <CSRFToken />
            <div className="form-field">
              <label htmlFor="validateAccountName">Account name</label>
              <input type="text"
                     name="name"
                     className="form-control is-valid"
                     id="validateAccountName"
                     onChange={this.handleChange}
                     placeholder="Account name" required />
              <div className="invalid-feedback">Please provide valid account name</div>
            </div>
            <div className="form-field">
              <label htmlFor="validatePassword">Password</label>
              <input type="password"
                     name="password"
                     className="form-control is-invalid"
                     id="validatePassword"
                     onChange={this.handleChange}
                     placeholder="Password" required />
              <div className="invalid-feedback">Please provide valid password</div>
            </div>
            <button className="btn btn-primary" type="submit">Submit form</button>
          </form>
        </div>
      </div>
    );
  }
}

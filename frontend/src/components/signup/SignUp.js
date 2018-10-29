import axios from 'axios';
import React, {Component} from 'react';

import {csrftoken_str} from './../csrf/csrftoken';
import Page404 from './../404/Page404';
import './SignUp.sass';


export default class SignUp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      email: '',
      password: '',
      password1: '',
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
    console.log(e.target.name, e.target.value)
  };

  handleSubmit = e => {
    e.preventDefault();
    console.log(e);
  };

  render() {
    return(
      <div className="container">
        <div className="row">
          <h1 className="col-12">Sign Up:</h1>
          <form className="sign-form" onSubmit={this.handleSubmit}>
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
              <label htmlFor="validateEmail">Email</label>
              <input type="email"
                     name="email"
                     className="form-control is-valid"
                     id="validateEmail"
                     onChange={this.handleChange}
                     placeholder="email" required />
              <div className="invalid-feedback">Please provide valid email</div>
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
            <div className="form-field">
              <label htmlFor="validatePassword1">Repeat Password</label>
              <input type="password"
                     name="password1"
                     className="form-control"
                     id="validatePassword1"
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

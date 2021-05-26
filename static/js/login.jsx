function LoginForm(props){
    const [email, setEmail] = React.useState('');
    const [password, setPassword] = React.useState('');
    
    function handleSubmit(evt){
      evt.preventDefault();
      fetch('/api/login', 
        {method: 'POST', 
        body: JSON.stringify({'email': email, 'password':password}), //the key is a string, the value is the piece of state
        headers: {'Content-type': 'application/json'} //needed so the server knows where to get the values out from
        })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        if (data !== null) {
          props.setUserInfo(data);
          console.log('nice login');
          alert('You are logged in. Go buy some melons!');
          // document.location.href = '/marketplace';
        } else {
          alert('Nope. That did not work. Try again?');
        }
 
      })
      
    }
 
    return (
              <div class="col">
              <h1>Come on in and Bid on Some Melons!</h1>
              <form onSubmit={(evt) => {handleSubmit(evt)}}>
                  <div class="form-group w-25">
                      <div class="col-xs-2">
                          <label>Email</label>
                          <input class="form-control" type="text" name="email" id="email" onChange={ evt => {
                              setEmail(evt.target.value)
                          }}/>
                      </div>
                      <div class="col-xs-2">
                          <label>Password</label>
                          <input class="form-control" type="password" name="password" id="password" onChange={ evt => {
                              setPassword(evt.target.value)
                          }}/>
                      </div>
                      <button type="submit" class="btn btn-primary active">Login</button>
                  </div>
              </form>
          </div>
      );

  }


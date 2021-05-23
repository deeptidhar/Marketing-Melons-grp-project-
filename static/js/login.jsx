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
          alert('Login successful');
        } else {
          alert('Incorrect email or password.')
        }

      })
    }
  
    return (
      <form onSubmit={(evt) => {handleSubmit(evt)}}>
        <label>Email</label>
        <input id='email' onChange={ evt => { setEmail(evt.target.value) } } />
        <label>Password</label>
        <input id='password' type='password' onChange={ evt => { setPassword(evt.target.value) } } />
        <input type='submit' />
      </form>
      )
  }
function App() {
  const [listings, setListings] = React.useState({});

  const [loading, setLoading] = React.useState(false);

  const [user, setUser] = React.useState(false);

  const [triggerUpdate, setTriggerUpdate] = React.useState(0);

  // Do this once, when the component mounts.
  React.useEffect(() => {
    setLoading(true);
    fetch("/api/listings")
      .then((response) => response.json())
      .then((listingData) => {
        console.log(listingData);
        setListings(listingData);
        setLoading(false);
      });
  }, [triggerUpdate]);

  return (
    <ReactRouterDOM.BrowserRouter>
      <Navbar logo="/static/img/watermelon.png" brand="BitMelon">
        <ReactRouterDOM.NavLink
          to="/marketplace"
          activeClassName="navlink-active"
          className="nav-link"
        >
          Bid on Melons
        </ReactRouterDOM.NavLink>
        <ReactRouterDOM.NavLink
          to="/login"
          activeClassName="navlink-active"
          className="nav-link"
        >
          Log In
        </ReactRouterDOM.NavLink>
      </Navbar>
      <div className="container-fluid">
      
      <ReactRouterDOM.Switch>
      
        <ReactRouterDOM.Route exact path="/">
          {loading ? (<Loading />) : (<Homepage />)}
        </ReactRouterDOM.Route>
      
        <ReactRouterDOM.Route exact path="/marketplace">
          {user ? (loading ? (<Loading />) : (<MarketplacePage setTriggerUpdate={setTriggerUpdate} user={user} listings={listings}/>)) : (<div>Log in to view this page</div>)}
        </ReactRouterDOM.Route>

        <ReactRouterDOM.Route exact path="/login">
          {loading ? (<Loading />) : (<LoginForm setUserInfo={setUser}/>)}
        </ReactRouterDOM.Route>

         {/* For any other URL, display page not found */}
         <ReactRouterDOM.Route path="*">
          <div>Page not found :(</div>
        </ReactRouterDOM.Route>

        </ReactRouterDOM.Switch>
        </div>
    </ReactRouterDOM.BrowserRouter>
  );
}

ReactDOM.render(<App />, document.querySelector("#root"));

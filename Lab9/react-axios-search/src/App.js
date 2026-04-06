import React, { useEffect, useState } from "react";
import { getUsers } from "./services/api";
import SearchBar from "./components/SearchBar";
import DataList from "./components/DataList";

function App() {
const [users, setUsers] = useState([]);
const [searchTerm, setSearchTerm] = useState("");
const [loading, setLoading] = useState(true);
const [error, setError] = useState("");

// Fetch data using Axios
useEffect(() => {
getUsers()
.then((response) => {
setUsers(response.data);
setLoading(false);
})
.catch(() => {
setError("Error fetching data");
setLoading(false);
});
}, []);

// Search filter
const filteredUsers = users.filter((user) =>
user.name.toLowerCase().includes(searchTerm.toLowerCase())
);

return (
<div style={{ textAlign: "center" }}>
<h1>React Axios Search App</h1>

<SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />

{loading && <p>Loading...</p>}
{error && <p style={{ color: "red" }}>{error}</p>}

{!loading && !error && <DataList data={filteredUsers} />}
</div>
);
}

export default App;

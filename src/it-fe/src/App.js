import axios from 'axios';
import React, {useEffect, useState} from 'react';
import {backend_url} from "./const";
import {
  BrowserRouter as Router,
  Routes, Route, Link
} from "react-router-dom"
import {HomeComponent} from "./components/Home";
import {CreateDBComponent} from "./components/CreateDBComponent";
import {CreateTableComponent} from "./components/CreateTableComponent";
import {AddRowComponent} from "./components/AddRowComponent";
import {ViewAndEditTableComponent} from "./components/EditTableComponent";
import {DedupTableComponent} from "./components/DedupTableComponent";
import {GetDumpComponent} from "./components/GetDumpComponent";
import {FromDumpComponent} from "./components/FromDumpComponent";

function App() {
  return (
      <>
        <Router>
          <div>
            <Link to="/"> Home </Link>
            <Link to="/create_db"> Create DB </Link>
            <Link to="/create_table"> Create table </Link>
            <Link to="/add_row"> Add row </Link>
            <Link to="/dedup_table"> Dedup table </Link>
            <Link to="/view_edit_table"> View and edit table </Link>
            <Link to="/get_dump"> Get dump </Link>
            <Link to="/from_dump"> Create from dump </Link>
          </div>
          <Routes>
            <Route path="/create_db" element=<CreateDBComponent /> />
            <Route path="/create_table" element=<CreateTableComponent /> />
            <Route path="/add_row" element=<AddRowComponent /> />
            <Route path="/dedup_table" element=<DedupTableComponent /> />
            <Route path="/view_edit_table" element=<ViewAndEditTableComponent /> />
            <Route path="/get_dump" element=<GetDumpComponent /> />
            <Route path="/from_dump" element=<FromDumpComponent /> />
            <Route path="/" element=<HomeComponent /> />
          </Routes>
        </Router>
      </>
  )
}

export default App;

import React, { useState } from "react";
import axios from "axios";
import { useEffect } from "react";
import Select from "react-select";

const App = () => {
  const [data, setData] = useState();
  const url = "http://127.0.0.1:8000";
  const [option, setOption] = useState("common");
  const options = [
    { value: "common", label: "共通" },
    { value: "engineering_department", label: "技術部門" },
    { value: "planning_department", label: "企画部門" },
  ];

  const GetData = (url) => {
    axios.get(url).then((res) => setData(res.data));
  };

  useEffect(() => {
    GetData(`${url}?value=${option}`);
  }, [option]);

  return (
    <div className="container">
      <Select
        className="mb-3"
        options={options}
        onChange={(value) => {
          setOption(value.value);
        }}
      />
      {data ? <h4>{data.name}</h4> : <h4></h4>}
      {data ? (
        <div className="d-flex flex-column gap-2 ">
          {data.items.map((data) => {
            return (
              <div className="linkList border p-2 d-flex flex-row align-items-center gap-1">
                {data.img_url ? (
                  <div className="favicon">
                    <img
                      src={data.img_url}
                      alt=""
                      className="img-fluid"
                      style={{ height: 20 }}
                    />
                  </div>
                ) : (
                  <div></div>
                )}
                <div className="dataName">{data.name}</div>
                <div className="dataUrl">{data.url}</div>
              </div>
            );
          })}
        </div>
      ) : (
        <div></div>
      )}
    </div>
  );
};

export default App;

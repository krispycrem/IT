import { ChangeEvent, useState } from 'react';
import axios from "axios";
import {backend_url} from "../const";

export const FromDumpComponent = () => {
    const [file, setFile] = useState();
    const [database, setDatabase] = useState();
    const [schema, setSchema] = useState("")
    const [isOK, setIsOK] = useState(false)
    const handleFileChange = (e) => {
        if (e.target.files) {
            setFile(e.target.files[0]);
        }
    };

    const handleUploadClick = async () => {
        const bodyFormData = new FormData();
        bodyFormData.append('dump', file)
        bodyFormData.append('database', database)
        bodyFormData.append('table_schema', schema)
        const result = await axios.post(`${backend_url}/database/read_dump`,
            bodyFormData,
            // { headers: {"Content-Type": "multipart/form-data"}}
        )
        console.log(result)
        if (result.status < 400) {
            setIsOK(true)
        }
    };

    return (
        <div>
            <p> Database Name </p>
            <input onChange = {event => setDatabase(event.target.value)} />
            <p> Schema </p>
            <textarea onChange = {event => setSchema(event.target.value)} />
            <p> Dump </p>
            <input type="file" onChange={handleFileChange} />
            <div>{file && `${file.name} - ${file.type}`}</div>
            <button onClick={handleUploadClick}>Upload</button>
            {isOK
                ? <b> OK, got dump! </b>
                : <></>}
        </div>
    );
}



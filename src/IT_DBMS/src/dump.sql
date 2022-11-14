--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: flowers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.flowers (
    id integer NOT NULL,
    name character varying,
    color character varying
);


ALTER TABLE public.flowers OWNER TO postgres;

--
-- Name: flowers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.flowers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.flowers_id_seq OWNER TO postgres;

--
-- Name: flowers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.flowers_id_seq OWNED BY public.flowers.id;


--
-- Name: flowers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flowers ALTER COLUMN id SET DEFAULT nextval('public.flowers_id_seq'::regclass);


--
-- Data for Name: flowers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.flowers (id, name, color) FROM stdin;
1	orchid	red
\.


--
-- Name: flowers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.flowers_id_seq', 2, true);


--
-- Name: flowers flowerspk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flowers
    ADD CONSTRAINT flowerspk PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--


--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- Name: booking_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.booking_table (
    booking_id integer NOT NULL,
    name character varying(100),
    phone_number character varying(15),
    email character varying(100),
    type_of_crop character varying(50),
    weight_of_crop integer,
    from_place character varying(100)
);


ALTER TABLE public.booking_table OWNER TO postgres;

--
-- Name: booking_table_booking_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.booking_table_booking_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.booking_table_booking_id_seq OWNER TO postgres;

--
-- Name: booking_table_booking_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.booking_table_booking_id_seq OWNED BY public.booking_table.booking_id;


--
-- Name: formers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.formers (
    fid integer NOT NULL,
    email character varying(100) NOT NULL,
    name character varying(100),
    type_of_crop character varying(100),
    delivery_date date,
    transport_date date,
    lot_number character varying(50),
    rent_cost integer,
    from_place character varying(100)
);


ALTER TABLE public.formers OWNER TO postgres;

--
-- Name: formers_fid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.formers_fid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.formers_fid_seq OWNER TO postgres;

--
-- Name: formers_fid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.formers_fid_seq OWNED BY public.formers.fid;


--
-- Name: storage_details; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.storage_details (
    id integer NOT NULL,
    empty_lot_normal_temp integer,
    empty_lot_deep_temp integer,
    empty_lot_very_deep_temp integer,
    total_empty integer
);


ALTER TABLE public.storage_details OWNER TO postgres;

--
-- Name: storage_details_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.storage_details_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.storage_details_id_seq OWNER TO postgres;

--
-- Name: storage_details_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.storage_details_id_seq OWNED BY public.storage_details.id;


--
-- Name: booking_table booking_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking_table ALTER COLUMN booking_id SET DEFAULT nextval('public.booking_table_booking_id_seq'::regclass);


--
-- Name: formers fid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.formers ALTER COLUMN fid SET DEFAULT nextval('public.formers_fid_seq'::regclass);


--
-- Name: storage_details id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.storage_details ALTER COLUMN id SET DEFAULT nextval('public.storage_details_id_seq'::regclass);


--
-- Data for Name: booking_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.booking_table (booking_id, name, phone_number, email, type_of_crop, weight_of_crop, from_place) FROM stdin;
1	Ravi Kumar	9876543210	ravi@farm.com	tomato ??	1000	Guntur
2	Lakshmi Devi	9845123456	lakshmi@farm.com	chilli ???	800	Warangal
3	Suresh Reddy	9956784321	suresh@farm.com	tobacco ??	1200	Rajahmundry
4	Anita Das	9123456780	anita@farm.com	fish ??	500	Kakinada
5	Mahesh Babu	9988776655	mahesh@farm.com	meat ??	700	Hyderabad
6	Kiran Kumar	9871203456	kiran@farm.com	apples ??	600	Shimla
7	Swathi Rao	9965432190	swathi@farm.com	cabbage ??	450	Vijayawada
8	Naresh Yadav	9898989898	naresh@farm.com	potatoes ??	950	Nellore
9	Pavani R	9001234567	pavani@farm.com	tomato ??	1100	Ongole
10	Vikram S	9876001122	vikram@farm.com	fish ??	550	Machilipatnam
\.


--
-- Data for Name: formers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.formers (fid, email, name, type_of_crop, delivery_date, transport_date, lot_number, rent_cost, from_place) FROM stdin;
1	nani@farm.com	Nani	meat	2025-04-01	\N	LOT042	2500	Hyderabad
2	siri@farm.com	Siri	fish	2025-04-02	\N	LOT043	2300	Machilipatnam
3	pinki@farm.com	Pinki	apples	2025-04-03	2025-04-07	LOT044	1900	Shimla
4	lokesh@farm.com	Lokesh	tomato	2025-04-04	\N	LOT045	1200	Guntur
5	swetha@farm.com	Swetha	chilli	2025-04-05	2025-04-10	LOT046	1500	Warangal
6	mani@farm.com	Mani	tobacco	2025-04-06	\N	LOT047	1700	Rajahmundry
7	sunil@farm.com	Sunil	potatoes	2025-04-07	\N	LOT048	1300	Nellore
8	varsha@farm.com	Varsha	cabbage	2025-04-08	\N	LOT049	1100	Kakinada
9	shiva@farm.com	Shiva	fish	2025-04-09	2025-04-12	LOT050	2200	Kakinada
10	anji@farm.com	Anji	meat	2025-04-10	\N	LOT051	2400	Vijayawada
\.


--
-- Data for Name: storage_details; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.storage_details (id, empty_lot_normal_temp, empty_lot_deep_temp, empty_lot_very_deep_temp, total_empty) FROM stdin;
1	4	3	2	9
2	5	2	1	8
3	6	4	3	13
4	2	1	1	4
5	3	5	2	10
6	1	0	0	1
7	7	2	2	11
8	6	3	1	10
9	5	4	3	12
10	3	3	2	8
\.


--
-- Name: booking_table_booking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.booking_table_booking_id_seq', 10, true);


--
-- Name: formers_fid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.formers_fid_seq', 10, true);


--
-- Name: storage_details_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.storage_details_id_seq', 10, true);


--
-- Name: booking_table booking_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking_table
    ADD CONSTRAINT booking_table_pkey PRIMARY KEY (booking_id);


--
-- Name: formers formers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.formers
    ADD CONSTRAINT formers_pkey PRIMARY KEY (fid);


--
-- Name: storage_details storage_details_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.storage_details
    ADD CONSTRAINT storage_details_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--


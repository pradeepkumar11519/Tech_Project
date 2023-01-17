import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import { QueryClient, dehydrate, useQuery, useMutation } from '@tanstack/react-query'
import axios from 'axios'
import InfiniteScroll from 'react-infinite-scroll-component';
import GridLoader from "react-spinners/GridLoader";
import { useContext, useState } from 'react'
import Context from '../../context/Context'
import TableElements from '../../components/TableElements'



export default function Compete() {

	let { nexturl, setnexturl } = useContext(Context)
	const test1 = useFetchContest()
	const AllContests = useQuery(['AllContests'], () => {
		return fetchAllContests(nexturl)
	}, {
		onSuccess: (data) => {
			setnexturl("http://127.0.0.1:8000/api/v1/ListAllContest")
			nexturl="http://127.0.0.1:8000/api/v1/ListAllContest"
			test1.mutate(nexturl)
		},
		refetchOnWindowFocus: false,
	})



	

	return (
		<div>
			<TableElements AllContests={AllContests}/>
		</div>
	)
}



const fetchAllContests = async (nexturl) => {
	return axios.get('http://127.0.0.1:8000/api/v1/ListContest/').then((response) => {
		return response.data
	})
}


const fetchContests = async (nexturl) => {
	return axios.get(nexturl)
}

const useFetchContest = () => {
	const { Contests, setContests, setnexturl } = useContext(Context)
	return useMutation(fetchContests, {
		onSuccess: (response) => {

			setContests(response.data.results)
			setnexturl(response.data.next)

		}
	})
}
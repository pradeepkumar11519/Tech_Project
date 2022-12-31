import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import { QueryClient, dehydrate, useQuery, useMutation } from '@tanstack/react-query'
import axios from 'axios'
import InfiniteScroll from 'react-infinite-scroll-component';
import GridLoader from "react-spinners/GridLoader";
import { useContext, useState } from 'react'
import Context from '../../context/Context'



export default function Compete() {
	
	const { invert,Contests,setContests,nexturl,setnexturl } = useContext(Context)
	let [count, setcount] = useState(0)
	const test1 = useFetchContest()
	const AllContests = useQuery(['AllContests'], () => {
		return fetchAllContests(nexturl)
	}, {
		onSuccess: (data) => {
			
			test1.mutate(nexturl)
		},
		refetchOnWindowFocus: false,
	})

	

	const fetchData = async () => {
		await axios.get(nexturl).then((response) => {
			
			setnexturl(response.data.next)
		
			setContests(Contests.concat(response.data.results))
		}).catch((e) => {
			
		})
	}

	if (AllContests.isLoading && !AllContests.isError && AllContests.isFetching) {
		return (<div className='mx-auto text-center my-20 flex items-center justify-center'><GridLoader /></div>
		)
	}
	
	return (
		<div>
			<div className=''>
				<div className=''>
					<div className={`${invert ? "invert" : ""} bg-white w-full ${AllContests.isLoading ? "h-screen" : "h-max"}  text-center z-[-1] py-32`} >
						<h1 className='text-center mb-24 font-bold text-3xl '>All Contests</h1>
						<div className={`mx-10`}>


							{!AllContests.isLoading && !AllContests.isError && (
								<>
									<div className=' border-2 border-black rounded-md'>
										<div className="grid-cols-[100px_auto] grid border-b-2 border-black font-bold bg-rose-600 rounded-t-md">
											<div className=" w-[100px] text-white  text-center p-2 uppercase">
												s.no
											</div>
											<div className="grid grid-cols-9 text-white uppercase">
												<div className="border-l-2 border-black w-full p-2  break-all">website name</div>
												<div className="border-l-2 border-black w-full p-2 col-span-2 break-all">Competetion name</div>
												<div className="border-l-2 border-black p-2 col-span-2 break-all">place</div>
												<div className="border-l-2 border-black p-2 break-all">start time</div>
												<div className="border-l-2 border-black p-2 break-all">duration</div>
												<div className="border-l-2 border-black  break-all p-2">Day To Start</div>
												<div className="border-l-2 border-black rounded-tr-md break-all  p-2">Days To Resgiter</div>
											</div>
										</div>
										<InfiniteScroll
											dataLength={Contests.length} //This is important field to render the next data
											next={fetchData}
											
											hasMore={nexturl !== null}
											loader={<div className='mx-auto text-center my-20 flex items-center justify-center'><GridLoader /></div>}


										>
											{Contests.map((contest) => {
												count = count + 1
												return (
													<div key={contest.id}>
														<div className={`grid-cols-[100px_auto] grid font-medium ${(contest.id) % 2 === 0 && !contest.OnGoing ? "" : "bg-slate-100"} ${contest.OnGoing && contest.id%2===0 ?"bg-green-500 bg-opacity-30":""} ${contest.OnGoing && contest.id%2!==0?"bg-green-500 bg-opacity-50":""}`}>
															<div className="border-2 border-transparent w-[50px] text-center">
																{count}
															</div>
															<div className="grid grid-cols-9">
																<div className=" break-all p-2  border-l-2 border-black"> {contest?.Name_Of_Website}</div>
																<div className=" break-all p-2 col-span-2 border-l-2 border-black"> {contest?.Name_Of_Contest}</div>
																<div className=" break-all p-2 col-span-2 border-l-2 border-black text-indigo-600"><Link href={contest?.Place}>{contest?.Place}</Link></div>
																<div className=" break-all p-2 border-l-2 border-black">{contest?.Start_Time}</div>
																<div className=" break-all p-2 border-l-2 border-black">{contest?.Contest_Duration}</div>
																<div className=" break-all p-2 border-l-2 border-black">{contest?.Days_Remaining_For_The_Contest_To_Start}</div>
																<div className=" break-all p-2 border-l-2 border-black">{contest?.Days_Remaining_To_Register}</div>
															</div>
														</div>


													</div>
												)
											})}

										</InfiniteScroll>

									</div>
								</>
							)
							}
							{
								!AllContests.isLoading && AllContests.isError && (
									<>{AllContests?.error?.message}</>
								)
							}
						</div >
					</div>
				</div>
				
			</div>
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

const useFetchContest = () =>{
	const {Contests,setContests,setnexturl} = useContext(Context)
	return useMutation(fetchContests,{
		onSuccess:(response)=>{
			
			setContests(response.data.results)
			setnexturl(response.data.next)
			
		}
	})
}
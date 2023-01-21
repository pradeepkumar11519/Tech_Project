import axios from 'axios';
import React, { useContext, useEffect,useState  } from 'react'
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import Context from '../../context/Context'
import {useQuery} from '@tanstack/react-query'
export default function Calender() {
  const {authtoken,CalenderContest,setCalenderContest} = useContext(Context)
  const [value, onChange] = useState(new Date());
  const [DateValue,setDateValue] = useState({Day:null,Month:null,Year:null})
 
  const [loading,setloading] = useState(false)
  
  const CalenderContests = useQuery(['CalenderContests'],()=>{
    return fetchCalenderContests()
  },{
    onSuccess:(data)=>{
      setCalenderContest(JSON.parse(data))
    }
  }
  
  )
  return (
    <div className='my-32 text-center mx-auto  justify-center grid grid-cols-2'>
      <div className=' flex justify-center'>
      <Calendar onChange={onChange}  value={value} onClickDay={async (value)=>{
        setloading(true)
        console.log(value.toString().slice(11,15))
        await axios.post 
         ('http://127.0.0.1:8000/api/v1/ListCalenderContests/',{
            day:value.toString().slice(8,10),
            month:value.toString().slice(4,7),
            year:value.toString().slice(11,15)
          
        },{
          headers:{
            Authorization:'Bearer ' + authtoken.access_token
          }
        }).then((response)=>{
          setCalenderContest(JSON.parse(response.data))
          console.log(response.data)
          setloading(false)
        }).catch(e=>console.log(e))
      }} />
      </div>
      <div className='border-2 border-black shadow-2xl mx-20'>
      <h1 className='font-bold text-center text-xl my-5'>YOUR CALENDER EVENTS</h1>
      {(CalenderContests.isLoading && loading && !CalenderContests.isError)?(
        <h1 className='text-center font-medium text-lg'>Loading...</h1>
      ):(
        (!CalenderContests?.isLoading && !loading && !CalenderContests?.isError && CalenderContest?.length!==0 && CalenderContests?.data?.length!==0)?(
          CalenderContest?.map((contest)=>{
            return (
              <>
            
            <div className='shadow-2xl border-2 border-black rounded-md p-2 mx-5 my-5'>
              <h1 className='font-bold text-lg'>Name Of Contest :</h1><p>{contest.contest_name}</p>
            </div>
            </>
            )})
            
        ):(
          <>
          <h1 className='text-center font-medium text-lg'>YOU HAVE CURRENTLY NOY ADDED ANYTHING</h1>
          </>
        )
      )}
      
        
       
      </div>
    </div>
  )
}


const fetchCalenderContests = async () =>{
  return axios.get('http://127.0.0.1:8000/api/v1/ListTodaysCalender/',{
    headers:{
      Authorization:'Bearer ' + localStorage.getItem('access_token')
    }}).then((response)=>{
    return response.data
  })
}
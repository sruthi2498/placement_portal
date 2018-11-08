//basic layout for blocking students
function func()
{
    //read student data
}

function check_eligiblity_gpa()
{
		student=func();
		if(student['gpa'] < company['gpa']) 
		{
			student['blocked']=='yes'
		}
}
function check_eligibility_tier()
{
		student=func();
		if(company['fte']=='yes' && company['internship']=='yes')
		{

			if(student['tier'] < company['tier'])
			{
				student['blocked']=='yes'
			}
		}
		else if(company['fte']=='yes'&& company['internship']=='no')
			{
				if(student['fte']=='yes')
				{
					student['blocked']=='yes'	
				}
			}
		else
		{
			if(student['internship']=='yes')
			{
				student['blocked']=='yes'
			}
		}			
}
   


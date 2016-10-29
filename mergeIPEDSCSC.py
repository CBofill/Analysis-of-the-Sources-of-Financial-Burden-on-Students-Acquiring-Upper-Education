#coding:utf-8
import pandas as pd
from numpy import isnan

# IPEDS csv files
ipeds_csv = ['delta_public_00_12.csv','delta_public_87_99.csv']

# IPEDS relevant features
ipeds_characteristics = ['iclevel','control','census_region','flagship','landgrnt','hbcu','hsi','medical','hospital']
ipeds_revenue = ['tuition01','tuition02','tuition03','nettuition01','net_student_tuition','federal03','state03','local03',
                 'state_local_app','federal07','federal07_net_pell','state06','local06','state_local_grant_contract','federal10',
                 'federal10_net_pell','state09','fed_state_loc_grants_con','private03','affiliate01','investment01','endowment03',
                 'priv_invest_endow','edactivity03','auxiliary03','hospital03','other03','other04','independent03','other05',
                 'auxother_rev','stable_operating_rev','total03_revenue','tot_rev_wo_auxother_sum','tot_rev_w_auxother_sum',
                 'unrestricted_revenue','restricted_revenue','tuition_reliance_a1','tuition_reliance_b1','tuition_reliance_c1',
                 'tuition_reliance_a2','tuition_reliance_b2','tuition_reliance_c2','govt_reliance_a','govt_reliance_b',
                 'govt_reliance_c']
ipeds_scholarships_fellowships = ['appliedaid01','appliedaid02','grant01','grant02','grant03','grant04','grant05','grant06',
                                  'grant07','institutional_grant_aid','institutional_grant_aid_share','tuition_discount']
ipeds_expenditures = ['instruction01','instruction01_fasb','instruction02','research01','research01_fasb','research02','pubserv01',
                      'pubserv01_fasb','pubserv02','acadsupp01','acadsupp01_fasb','acadsupp02','studserv01','studserv01_fasb',
                      'studserv02','instsupp01','instsupp01_fasb','instsupp02','opermain01','opermain01_fasb','opermain02',
                      'depreciation01','grants01u','grants01r','grants01','grants01_fasb','auxiliary01','auxiliary01_fasb',
                      'auxiliary02','hospital01','hospital01_fasb','hospital02','independ01','independ01_fasb','independ02',
                      'otheroper01','otheroper02','totaloper01','totaloper02','totaloper03','totaloper04','totaloper05',
                      'interest01','othernon01','othernon02','other01','other01_fasb','other02','totalnon01','totalnon02',
                      'total01','total02','total03_expenses','total04','total05','total06','total07','eandg01','eandg01_sum',
                      'eandg01_w_auxother_sum','eandg02','eandg03','eandg03a','eandg03b','eandg04','eandg05','eandg06','eandg07',
                      'eandg08','rschpub01','acadinststud01','acadinstsupp01','education_share','noneducation_share',
                      'other_ed_related_cost','instruction_share','studserv_share','admin_share','eandr','eandr_degree',
                      'eandr_completion','research_share','research_related_cost','pubserv_share','pubserv_related_cost',
                      'research_pubserv_grants','auxother_cost','sticker_subsidy','average_subsidy','sticker_price_share',
                      'nettuition_share','average_subsidy_share','gross_auxiliary_margin','gross_auxiliary_margin_percent',
                      'gross_operating_margin','fringe_benefit_play','fringe_benefit_play_imp','instr_sal_as_pct_instrtot',
                      'labor_share_of_instructcost','research_sal_as_pct_restot','labor_share_of_rescost',
                      'acadsupp_sal_as_pct_acadsupptot','labor_share_of_acadsuppcost','studserv_sal_as_pct_studservtot',
                      'labor_share_of_studservcost','instsupp_sal_as_pct_instsupptot','labor_share_of_instsuppcost',
                      'pubserv_sal_as_pct_pubservtot','labor_share_of_pubservcost']
ipeds_assets = ['assets06','liabilities07','assets11','land04','buildings05','equipment05','assets15','endow02m','assets16']
ipeds_faculty = ['conthoursug','credhoursgr','credhoursug','ftall1','ftall3','ftall4','ftall5','ftall6','ftall7',
                 'ftall8','ptall1','ptall2','ptall3','ptall4','ptall5','ptall6','ptall7','ptall8','ft_faculty_per_100fte',
                 'pt_faculty_per_100fte','total_executive_admin_managerial','ft_executive_per_100fte','pt_executive_per_100fte',
                 'total_other_professionals','ft_other_professional_per_100fte','pt_other_professional_per_100fte',
                 'total_technical_and_paraprof','ft_technical_per_100fte','pt_technical_per_100fte','total_clerical_secretarial',
                 'ft_clerical_per_100fte','pt_clerical_per_100fte','total_skilled_craft','ft_skilled_per_100fte',
                 'pt_skilled_per_100fte','total_service_maintenance','ft_service_per_100fte','pt_service_per_100fte',
                 'ft_exec_admin_man_share','ft_other_professional_share','ft_technical_paraprof_share',
                 'ft_clerical_secretarial_share','ft_skilled_craft_share','ft_service_maintenance_share','total_faculty_all',
                 'full_time_employees','full_time_employee_share','all_employees','ft_faculty_salary','full_time_employee_100fte',
                 'full_time_faculty_share','faculty_instr_headcount','salarytotal']
ipeds_graduation_rates = ['grad_rate_150_n','grad_rate_150_p','grad_rate_adj_cohort_n','grad_rate_150_n4yr','grad_rate_150_p4yr',
						  'grad_rate_adj_cohort_n4yr','grad_rate_150_n2yr','grad_rate_150_p2yr','grad_rate_adj_cohort_n2yr']
ipeds_enrollment = ['ugentering','ftretention_rate','ptretention_rate','fall_cohort_num','fall_cohort_pct',
					'fall_cohort_num_indistrict','fall_cohort_pct_indistrict','fall_cohort_num_instate','fall_cohort_pct_instate',
					'fall_cohort_num_outofstate','fall_cohort_pct_outofstate','fall_cohort_num_resunknown',
					'fall_cohort_pct_resunknown','fall_total_undergrad','year_cohort_num','year_cohort_pct','year_total_undergrad',
					'ft_first_time_first_yr_deg_seek','other_full_time','total_full_time_undergraduates',
					'returning_to_total_undergraduate','total_full_time_first_prof','total_full_time_graduates',
					'total_full_time_postbacc','total_full_time','pt_first_time_first_yr_deg_seek','other_part_time',
					'total_part_time_undergraduates','total_part_time_first_prof','total_part_time_graduates',
					'total_part_time_postbacc','total_part_time','total_undergraduates','total_graduates','total_first_prof',
					'total_postbacc','total_enrollment','total_enrollment_amin_tot','total_enrollment_asian_tot',
					'total_enrollment_black_tot','total_enrollment_hisp_tot','total_enrollment_white_tot',
					'total_enrollment_multi_tot','total_enrollment_unkn_tot','total_enrollment_nonres_tot',
					'ftug_share_of_total_ft_enrl','ptug_share_of_total_pt_enrl']
ipeds_degree_proportions = ['assoc_deg_share_of_tot_deg','bach_deg_share_of_tot_deg','grad_deg_share_of_tot_deg',
							'doc_deg_share_of_tot_deg','prof_deg_share_of_tot_deg']

hepi_scalar = ['hepi_scalar_2012']

# Complete feature list
ipeds_features = (ipeds_revenue + ipeds_scholarships_fellowships + ipeds_expenditures + ipeds_assets + ipeds_faculty + 
                  ipeds_graduation_rates + ipeds_enrollment + ipeds_degree_proportions + ipeds_characteristics + hepi_scalar)

# Return a dataframe composed of selected features from ipeds csv files
def read_ipeds():
	ipeds = pd.DataFrame(index=[['UnitID'],['Year']])
	ipeds.index.names = ['unitID','year']
	for csv in ipeds_csv:
		print "Reading file {}...".format(csv)
		full_data = pd.read_csv(csv,sep=',',index_col=['unitid','academicyear'])
		full_data.index.names = ['UnitID','Year']
		
		# Select desired feature set from full dataset
		selected_data = full_data.loc[:,ipeds_features]

		ipeds = ipeds.append(selected_data)
	
	ipeds = coerce_type(ipeds)
	
	return ipeds

# College Scorecard csv files
csc_csv = ['MERGED1997_PP.csv','MERGED1998_PP.csv','MERGED1999_PP.csv','MERGED2000_PP.csv','MERGED2001_PP.csv','MERGED2002_PP.csv','MERGED2003_PP.csv','MERGED2004_PP.csv','MERGED2005_PP.csv','MERGED2006_PP.csv','MERGED2007_PP.csv','MERGED2008_PP.csv','MERGED2009_PP.csv','MERGED2010_PP.csv','MERGED2011_PP.csv','MERGED2012_PP.csv']

# College Scorecard relevant features
csc_features= ['GRAD_DEBT_MDN','gt_25k_p6','gt_25k_p7','gt_25k_p8','gt_25k_p9','gt_25k_p10']

# Return a dataframe composed of selected features from csc csv files
def read_csc():
	csc = pd.DataFrame(index=[['unitID'],['year']])
	csc.index.names = ['unitID','year']
	for csv in csc_csv:
		print "Reading file {}...".format(csv)
		full_data = pd.read_csv(csv, sep=',',index_col='﻿UNITID') # Inexplicably there is a zero width no-break space in the UnitID header. It's invisible, but it's there.
		full_data.index.names = ['unitID']
		
		# Select desired feature set from full dataset
		selected_data = full_data.loc[:,csc_features]

		# Create a repeating series of the file's year with indices matching the file
		year = pd.Series(data=[int(csv[6:10])]*selected_data.shape[0],index=selected_data.index)

		# Append it to the dataframe, then drop it into the index
		selected_data['year'] = year
		selected_data.set_index('year',append=True,drop=True,inplace=True)

		csc = csc.append(selected_data)
	
	csc = coerce_type(csc)
	
	return csc

# Cast mixted type columns to float, coercing all missing data to NaN
def coerce_type(df):
	# List features with mixed type
	mixed_type = []
	for column in df:
		if df[column].dtype == 'object':
			mixed_type.append(column)
	
	# Cast features to float
	for feature in mixed_type:
		df[feature] = pd.to_numeric(df[feature],errors='coerce')
	
	return df

# Remove rows with no data in an output feature
def remove_missing_output(df):
	missing_data = []
	for unit in df.index.levels[0]:
		if df.loc[unit,['gt_25k_p6','gt_25k_p7','gt_25k_p8','gt_25k_p9','gt_25k_p10']].isnull().all().all():
			missing_data.append(unit)
		elif df.loc[unit,:]['GRAD_DEBT_MDN'].isnull().all():
			missing_data.append(unit)
		elif df.loc[unit,ipeds_degree_proportions].isnull().all().all():
			missing_data.append(unit)
	trimmed_data = df.drop(missing_data, level='unitID')

	return trimmed_data
	
# Compile IPEDS and CSC data, write to csv
def mergeIPEDSCSC():
	ipeds = read_ipeds()
	csc = read_csc()
	data = ipeds.merge(csc,left_index=True,right_index=True,how='inner')
	data = remove_missing_output(data)
	data.to_csv('MergedDataset.csv',sep=',',index_label=['unitID','year'])
   
mergeIPEDSCSC()
    

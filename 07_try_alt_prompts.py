from utils import classify_and_tag

areas = [
    "Education (e.g., safe and healthy schools)",
    "Workforce (e.g., income inequality)",
    "Health system reform and improvement",
    "Health services (quality and delivery)",
    "Health equity",
    "Violence prevention and interruption",
    "Housing",
    "Aging and disability",
    "Food security",
    "Maternal and child health and welfare",
    "Substance use disorder",
    "Mental health and suicide prevention",
    "Diseases and vaccinations",
    "Environmental justice (e.g. water quality, pollution)",
    "Sexual and reproductive health"
]

classify_prompt = f'''
    You are reviewing project abstracts to detect if this project is related to public health. You are a public health
    expert.
    
    Here's a definition to use: the science of protecting and improving the health of people and their 
    communities through promotion of healthy lifestyles, research for disease and injury 
    prevention, and detection and control of infectious diseases. Public health 
    professionals work to prevent problems from happening or recurring by implementing educational 
    programs, recommending policies, administering services, and conducting research. 
    Public health is concerned with protecting the health of entire populations, ranging 
    from a local neighborhood to an entire country or region of the world. Public health also 
    works to limit health disparities and promote health care equity, quality, and accessibility. Use an expansive definition
    of public health, including projects with secondary public health effects. Examples of project areas that could be 
    related to public health: {areas}
    
    Here are some examples of project abstracts with classifications:
    
    Example abstract of a directly related public health project: The AHRQ Quality Indicators (QIs), which rely on 
    readily available inpatient hospital claims data, can be used to pinpoint patient safety problems, 
    identify opportunities for improvement, and track hospital performance over time. After 20 years of development, 
    AHRQ seeks to review and potentially reduce the number of measures. AIR will synthesize the scientific evidence 
    and obtain expert opinion to help inform decisions about the future of the AHRQ Quality Indicator (QI) program, 
    including indicators to prioritize, retain, and refine for use in quality improvement initiatives. Specific tasks 
    include conducting a literature review and environmental scan on each indicator; submitting a request for 
    information to gather input from stakeholders about the usefulness of QIs for quality improvement; convening an 
    expert workgroup to seek input on the reliability, validity, and feasibility of the QIs and the rationale for 
    continued maintenance of each indicator as a quality improvement tool in the AHRQ QI program; and producing a 
    final report summarizing and synthesizing the evidence from previous activities. Example abstract of a project 
    with secondary public health effects (and so should be tagged as public health): USAID’s Famine Early Warning 
    System Network (FEWS NET) Project is the agency’s longest-running activity. Created in 1985 by the U.S. Agency 
    for International Development (USAID) after devastating famines in East and West Africa, FEWS NET provides 
    analysis for eight months out in advance on food insecurity in highly vulnerable countries around the world. The 
    FEWS NET Learning and Data Hub (“the Hub”) Task Order develops and manages the data and information platforms of 
    the FEWS NET Project, so these are accessible as evidence-based decision support products for USAID and other 
    U.S. government and international entities. The Hub has three work streams to support the FEWS NET Project: a 
    website platform for sharing FEWS NET analysis and data; a data warehouse management using secure, open, 
    intuitive, and accessible cloud-based tools; and knowledge management of information, a learning platform, 
    communications support, and supporting collaboration activities. 
    
    Example abstract of a project unrelated to public health: Secure UCEQA capacity for item and test development and 
    test structure/content quality assurance  Deliverable: Continue building institutional capacity within the UCEQA 
    system so that by project end, UCEQA will incorporate and make use of the most recent developments in educational 
    assessment that will make it a modern testing agency.  AIR will provide technical assistance by:  Providing UCEQA 
    with item and test analysis and review and targeted technical assistance for MFL content specialists (with 
    assistance from American Councils); Supporting construction of tests in MFL subjects (with assistance from 
    American Councils); Assisting UCEQA in developing an audio component for the MFL tests (with assistance from 
    American Councils); NOTE: This deliverable has been deleted from AIR’s contract on AC approval Assisting UCEQA in 
    introducing holistic scoring rubrics for MFL essay scoring, both in terms of holistic scoring rubric development 
    and scorer trainings (with assistance from American Councils); Advising/training UCEQA in advanced item 
    development techniques (with assistance from American Councils); Assisting UCEQA in special needs test 
    development (with assistance from American Councils). NOTE: This deliverable has been deleted from AIR’s contract 
    on AC approval 
    
    At the end of this message, you'll be given a new abstract. Classify whether or not this abstract is related to 
    public health. Some records may not have any text or may have text that is not really an abstract. In those cases, 
    return "unknown". Otherwise, return "Yes" if it is an abstract
    related to public health and "No" if it is not related to public health. 
    
    Return you response in the following format, replacing the values in brackets with your response:
    "Verdict: [Yes/No/Unknown] 
     
    Justification: [Explain why you chose your verdict]
    "
    
    Here is the project title and abstract: 
'''

tag_prompt = f'''
    You are reviewing abstracts for projects related to public health. Review the abstract below and determine
    which of the categories best applies to the abstract. Return only the category with which you feel is best.
    If none of the categories are appropriate, return "None".

    Categories:{areas}

    Here is an example of what an abstract from each category could look like:

    "Education (e.g., safe and healthy schools)": "The National Board of Professional Teaching Standards (NBPTS) is 
    partnering with AIR to examine whether National Board-certified teachers (NBCTs) impact students’ social and 
    emotional development in a way that differs from non-NBCTs. Change the Work is Intended to Produce or Contribute 
    To Original plan: We will evaluate approximately 70 K-3 teachers in various school districts to determine whether 
    NBCTs and non-NBCTs differ in how they contribute to students’ SEL. We consider NBCTs to be the intervention 
    group, and paired non-NBCTs teachers at the same grade level in the same school to be the comparison group. We 
    are specifically seeking districts that do not have an existing, districtwide SEL initiative, which we would 
    expect to be confounded with teachers “business-as-usual” condition. Students’ SEL will be assessed via SELWeb, 
    a validated direct SEL assessment. AIR will use a quasi-experimental design for the evaluation. This research 
    will contribute to the field’s understanding of how teachers influence social and emotional development of young 
    students in classroom settings. Further, the study will help schools and districts to understand students’ social 
    and emotional competencies. Post COVID plan: the study will address the same research questions but using 
    archival data as primary data collection is not an option within the study timeline." 
    
    "Workforce (e.g., income inequality)": The rates of labor participation and employment are significantly lower 
    for individuals with visual impairments compared with their nondisabled peers, both nationally and in 
    Massachusetts. Improving labor market outcomes for this group has become an increasingly important endeavor as 
    the visually disabled population is expected to double in the next few decades due to a multitude of factors, 
    including a rapidly aging U.S. population, the increase in prevalence of diabetes, and other chronic diseases. To 
    address this need, Massachusetts Commission for the Blind is looking to develop an ad campaign and Project Pep 
    Talk video series to (a) build employer awareness of how visually impaired individuals can play a productive role 
    in the business; (b) improve engagement of eye professionals to help connect vision impaired individuals with 
    vocational rehabilitation agencies and services; and (c) continue to engage this population and provide quality 
    vocational rehabilitation services. 

    "Health system reform and improvement": IMPAQ International will supplement Health System Transformation (HST) in 
    their support of the Vermont Legislative Joint Fiscal Office’s (JFO) six-member Legislative Task Force on 
    Affordable, Accessible Health Care (Task Force). IMPAQ will provide senior-level experts in the field of publicly 
    funded health care as well as research analyst/associate level task support. Under HST’s direction, IMPAQ will 
    provide analytic and subject matter expertise to: research, analyze, and report on relevant, actionable, 
    and impactful opportunities to increase access and affordability of healthcare in Vermont; support development 
    and implementation of a work plan to produce findings and recommendations regarding the most cost-effective ways 
    to expand access to affordable health care for Vermonters; and analyze various options available to implement 
    these recommendations. 

    "Health services (quality and delivery)": The Pennsylvania Dyslexia Screening and Early Literacy Intervention 
    Pilot Program Extension Study includes two main tasks. The first task is to support the Pennsylvania Department 
    of Education (PDE) in designing an implementation survey to be administered among classroom teachers and reading 
    interventionists to understand implementation during the extension period. In addition to survey development 
    consultation, AIR will provide data processing services and analyze the survey data. The second task is conduct 
    new analysis of student DIBELS (Dynamic Indicators of Basic Early Literacy Skills) data in the five continuing 
    districts to examine the effects of the small-group intervention on student literacy skills. 

    "Health equity": As the field of health care measurement has evolved, it has done so in ways that reflect 
    researcher, clinician, payer, and policymaker priorities. As a result, there is a critical gap - current 
    measurement approaches are not patient-centered, and often do not align with patient and family preferences and 
    values. In prior work, the American Institutes for Research (AIR) developed five principles for making 
    measurement patient-centered. Additional work is needed to demonstrate how to apply these patient-centered 
    measurement (PCM) principles in real-world settings. This project aims to: 1) Fund small-scale pilot projects 
    that test ways to implement the PCM principles; 2) Identify best practices from the pilot projects; and 3) 
    Facilitate shared learning about PCM principles among key stakeholders. To accomplish these aims, we will develop 
    a funding announcement and issue up to four pilot project awards. We will monitor implementation progress across 
    pilots and also facilitate a cross-pilot learning collaborative that includes quarterly meetings. To mitigate 
    potential implementation challenges, we will provide limited technical assistance to the pilot projects. Finally, 
    we will collect and disseminate best practices and lessons learned from the pilots about how to implement PCM, 
    engaging key stakeholders in the dissemination of this work. Throughout the project, we will ensure a focus on 
    patient-centeredness by including patient partners on our own team and requiring that pilot projects do the same. 
    
    "Violence prevention and interruption": Project Scope Abstract AIR received a subcontract from PowerTrain, Inc., 
    to deliver the Department of Defense (DoD) SPARX Knowledge training 26 times between September 13, 2021, 
    and September 30, 2022. DoD SPARX Knowledge is a 60-hour training delivered in a virtual classroom environment 
    over 2 weeks by a team of three trainers. It builds the capacity of military prevention professionals to prevent 
    suicide, sexual assault, harassment, child abuse and neglect, intimate partner violence, and substance abuse by 
    teaching them how to align their work with the current state of prevention science. Participants learn how to 
    execute a multi-step, data-driven prevention process: (1) understand the nature and magnitude of problematic 
    behaviors within the military, including contributing factors; (2) develop a comprehensive prevention approach; (
    3) implement prevention programs, practices, and policies with quality; and (4) conduct evaluation to inform 
    continuous quality improvement and determine which prevention activities should be sustained and which ones 
    should be discontinued. 

    "Housing": AIR and its team developed a Guide to Nursing Home Antimicrobial Stewardship (the Guide). The purpose 
    of the Guide is to make better decisions regarding antimicrobial prescribed for nursing home residents. The AIR 
    team pilot tested the Guide at three nursing home sites, modify it and then evaluated it in 9 sites. Nursing home 
    residents have high rates of infection and concomitant antimicrobial use, which makes infection control a vital 
    patient safety and quality improvement concern in nursing homes. Polypharmacy, or the use of multiple 
    medications, is the rule rather than the exception in nursing homes. In addition, as many as 40 percent of all 
    prescriptions are for antimicrobial agents, and some studies suggest that as many as 25 to 75 percent of these 
    medicines are inappropriately prescribed. High rates of antimicrobial use have been linked to the growth of 
    colonies of multi-drug resistance organisms, such as Clostridium difficile and methicillin-resistant 
    Staphylococcus aureus (MRSA). Thus, this type of inappropriate prescribing results in negative outcomes, 
    including adverse drug events, hospital admissions, higher health care costs, and antimicrobial resistance. 
    Helping clinicians and patients understand the importance of using antimicrobials appropriately is recognized as 
    a vital step towards reducing resistance to antimicrobials. The Guide produced through this project provides 
    nursing homes with a set of tools to choose from to implement antimicrobial stewardship practices, 
    including readiness assessment tools to ensure that nursing homes choose approaches that have the greatest chance 
    of success at their facilities. The Guide was pilot-tested in three nursing homes. Following the pilot, 
    the Guide was disseminated and evaluated in a sample of 9 nursing homes. We collected data on infections and 
    prescribing patterns to assess whether any changes in prescribing patterns occurred, conduct interviews to 
    evaluate the effectiveness and usefulness of the Guide, and analyze cost data to assess whether using the Guide 
    decreases any costs related to antibiotic use in nursing home residents. 
    
    "Aging and disability": Abstract: The purpose of the Individuals with Disabilities Education Act (IDEA) Analysis, 
    Communication, Dissemination, and Meetings (ACDM) Support contract is to provide the U.S. Department of 
    Education, Office of Special Education Programs (OSEP) with assistance in implementing five types of activities: 
    (1) development and dissemination of technical assistance and communication products; (2) quick turnaround 
    analyses of program issues; (3) analytical and logistical support for meetings and project reviews; (4) 
    activities to promote program improvement and strengthen outcomes and accountability of IDEA grantees; (5) 
    ownership, operation, maintenance, and enhancement of a project website; and (6) an optional task to support IDEA 
    Reauthorization activities once the law is reauthorized. 

    "Food security": IMPAQ International, LLC (IMPAQ) will conduct the endline evaluation of the current 
    McGovern-Dole (MGD) Food for Education (FFE) program “Support for the Integrated School Feeding Program” (
    2016–2020), as well as for the baseline evaluation of the next MGD FFE program (2021–2026) in Côte d’Ivoire. As 
    part of the FFE program, WFP provides school meals to 125,000 targeted children across grades 1 through 6 in 613 
    rural primary schools. Additionally, 50,000 girls are supported through take-home rations to alleviate hunger, 
    reduce food insecurity, and improve rates of school enrollment and attendance. Targeted children in these six 
    grades also benefit from complementary services, such as access to school gardens to enhance nutrition, 
    deworming, communication-related activities to influence social behaviors, and educational tools and reading 
    materials to improve learning. Other program beneficiaries, besides students from grades 1 through 6, 
    include school canteen staff, members of school management committees (SMCs), members of women’s production 
    groups (WPGs), teachers, principals, and households. WFP works to strengthen the capacities of these stakeholders 
    with the goal of improving students’ literacy, health, and nutrition. Finally, WFP provides technical and 
    financial support to 50 WPGs established near target schools to increase community participation in the school 
    feeding program and ensure sustainability of the school canteens. 
    

    "Maternal and child health and welfare": AIR is the evaluation lead for Phase II of the place-based initiative 
    called the Birth through Eight Strategy for Tulsa (BEST), funded by the George Kaiser Family Foundation (GKFF) in 
    Tulsa, Oklahoma. BEST seeks to transform Tulsa by improving the life circumstances of children from birth to age 
    8 years. BEST targets the entire birth-to-eight continuum, including prenatal care, preconception services, 
    childcare, preschool, and elementary school and, at its core, is a systems-change strategy rooted in the Tulsa 
    community. BEST also explicitly seeks to address inequity by reducing the extent to which the circumstances of a 
    child’s birth are a factor in the child’s health, well-being, development, and future success. By working with 
    over 20 participating community organizations, BEST seeks to create a new, sustainable system that leverages 
    human and data infrastructure to connect families to quality programs and services. As a result, BEST’s goal is 
    more of Tulsa’s children will be (1) born healthy, (2) on a positive developmental trajectory by age three, 
    (3) ready for kindergarten and (4) achieving success by third grade, thus preparing them to break free from 
    intergenerational poverty. AIR is responsible for designing and conducting a comprehensive place-based evaluation 
    that includes a process (including tracking system-level changes), outcomes and impact study components, 
    which is projected to be six years in duration. The initial 6 months of the project, (the engagement phase), 
    is focused the development of the mixed-method evaluation plan. It is expected after the plan is confirmed, 
    execution of the research study will begin in January 2020. 
    
    "Substance use disorder": Howard University Hospital (HU) and Unity Health Care (UHC) Inc. propose to implement a 
    program called Screening Brief Intervention and Referral to Treatment (SBIRT) in collaboration with the largest 
    Federal Qualified Health Center (FQHC) in Washington, D.C. The program aims to address alcohol or other substance 
    misuse among patients receiving services in their primary care or prenatal clinics, Emergency Department, 
    or inpatient obstetrics, medical, or surgical units. The project will provide universal SBIRT in these settings, 
    ensure linkage to and retention in substance use disorder treatment for those identified as needing treatment, 
    and increase treatment capacity. The program will serve a population of approximately 160,000, including 
    adolescents and adults primarily from low-income, diverse minority and ethnic groups residing in medically 
    underserved areas. The project will be guided by internal and external advisory boards, including leading experts 
    in SBIRT and addiction medicine, clinical faculty, and representatives from the District of Columbia's Department 
    of Behavioral Health. 
    
    "Mental health and suicide prevention": AIR is a subawardee to the School of Public Health at Indiana University, 
    Bloomington, on a new SAMHSA grant award to conduct the National Evaluation of SAMHSA’s Technology Transfer 
    Center (TTC) Program. Working with the School’s center, “Prevention Insights”, AIR’s piece of the work focuses 
    primarily on formative research through document review, KIIs and qualitative analysis to identify and understand 
    the individual program designs and plans for how each of the 39 TTC grantees are fulfilling SAMHSA’s mission for 
    the TTCs to develop and strengthen the behavioral healthcare and related healthcare workforce through the 
    dissemination of evidence based practices (EBPs). AIR’s work will help establish the evaluation design and data 
    collection tools. In FY 2018, SAMHSA reconfigured its approach to training and technical assistance by 
    establishing a national network of regional TTCs for substance use prevention and mental health services—adding 
    to an already established structure for addiction technology transfer centers (ATTCs). The fundamental premise of 
    this new approach was the broad dissemination of evidence-based practices to best equip the behavioral healthcare 
    and healthcare workforce with the skills needed to address substance use prevention and the treatment of mental 
    and substance use disorders, regardless of whether individual members of the workforce were themselves 
    beneficiaries of SAMHSA grant funding. The purpose of the National Evaluation is to gauge the extent to which 
    this effort has been effective and whether TTCs are achieving their intended purpose to grow the skills of the 
    workforce and to change clinical practice to deliver evidence-based services to communities nationwide. The 
    two-year evaluation grant has the bulk of AIR’s work occurring in the first year. The work fits in well with 
    other projects in our group that seek to better understand and improve provider knowledge and use of EBPs. It 
    also connects us with a university grounded in sound prevention science and represents a new win in SAMHSA 
    spanning its interests across prevention and treatment as well as across substance use and mental health. 
    
    "Diseases and vaccinations": Although there has been some progress in increasing vaccination uptake, reducing racial 
    and ethnic disparities in 
    vaccination rates, and reducing income disparities in vaccination rates, disparities in U.S. child and adolescent 
    vaccination rates remain, especially between urban and rural areas. Vaccination rates for young children (19 to 
    35 months old) in rural areas were lower for nearly all recommended vaccines, especially the measles, mumps, 
    and rubella vaccine (MMR), with a 6.9 percentage point urban-rural gap. The same trend holds true for adolescents 
    (13 to 17 years old) in rural areas recommended to receive the human papillomavirus (HPV) and meningococcal 
    vaccines; their rates of vaccination were 10 and 12 percentage points lower, respectively, than those living in 
    urban areas. To better understand child and adolescent vaccination disparities in rural areas, AIR will work with 
    the Centers for Disease Control and Prevention (CDC) to interview health care providers, parents, and community 
    leaders in three different rural areas to learn more about their knowledge, beliefs, and attitudes toward 
    vaccination and explore the facilitators of and barriers to receiving and providing vaccinations to children and 
    adolescents. We will conduct six to eight interviews per participant group. 

    "Environmental justice (e.g. water quality, pollution)": "Abstract: In this project, we will test what are the 
    changes in agricultural practices that will lead to greater uptake of neglected crops – diverse, regional plant 
    species that are typically nutrient-dense – in order to improve smallholder farmers’ well-being, 
    including maternal and child health in the Shinyanga region in Tanzania. The program will deliver a package of 
    complementary activities to promote the production and consumption of neglected crops. Key program components 
    are: (C1). Access to certified seeds and fertilizer for the neglected crops introduced; (C2). Agricultural 
    extension trainings for the production of neglected crops, including legume diversification and inter-cropping, 
    post-harvest management, and climate change adaptation; (C3). Nutrition trainings to women farmers to discuss the 
    nutritional characteristics of neglected crops and how to use them as part of their daily diets. These program 
    activities will help address some of the key barriers in new crop adoption such as credit constraints, 
    risk aversion, and information on new crop use. First, C1 will make seeds and fertilizer available during a 
    limited period so that credit constraints won’t affect adoption due to high initial investment costs under 
    uncertainty. Second, the program puts great emphasis into building the capacity of farmers through continuous 
    trainings on agricultural (C2) and nutritional (C3) topics given that farmers may view neglected crops adoption 
    as a risky investment as they need to learn a new practice in an environment with little insurance coverage. 
    Lastly, the program will link farmers with a reliable set of input suppliers, something key in an environment 
    where seeds and pesticides counterfeiting of common." 

    "Sexual and reproductive health": Recent and ongoing political and legislative changes intended to severely 
    restrict or eliminate abortion services present significant challenges to individuals seeking this care. Certain 
    groups, including persons of color and those living in poverty and in rural areas, are already challenged to 
    obtain this care due to economic and travel considerations. As the number of clinics that can deliver this care 
    decreases and the restrictions placed on remaining clinics increases, this inequity becomes greater. To better 
    understand the impact of these challenges on patients who are most affected and the stakeholders who serve them, 
    AIR is working with the Planned Parenthood Federation of America (PPFA) along with project collaborators 
    including independent abortion providers, local abortion funds, the National Abortion Federation, the National 
    Network of Abortion Funds, and other reproductive health, rights, and justice organizations such as the Abortion 
    Care Network and Resources for Abortion Delivery to conduct a qualitative study to assess the cultural, 
    structural, logistical, financial, and other types of supports patients desire when locating, scheduling, 
    accessing, and navigating abortion care and related services and supports. This project will include an 
    environmental scan, in-depth interviews with patients and stakeholders and focus groups with patients to refine 
    their knowledge of existing and best practices related to coordination of care and logistical supports, 
    as well as patient attitudes and preferences related to those supports. 

    Now based on this, assign a category to the abstract below. 
    
    Here is the project title and abstract:
'''

classify_and_tag('expansive thinking_areas_one shot', classify_prompt, tag_prompt)
AI-Guided Discovery of a Phage-Inspired Antibiotic Class with Anti-Biofilm and DNA 1 
Supercoiling Relaxation Activities 2 
 3 
Huan Chen1,2#, Yingqi Xu3#, Zhaoping Xiong4#, Hongliang Wang1#, Xin Wang1,2,, Yue Kang1,2,, Zhonglin 4 
Wang2,,  Xiaoyan Zeng2,Yahui Liu5, Yehuan Zheng1,2, Wei Chen1,2, Mengzhe Li6, Zhenyue Hu1,2, Chi Xu4, 5  Yue Wu2, Yawen Wang1,2, Zuyi Yuan2, Shuai Yuan7, Huadong Liu8, Steve Matthews3*, Nan Qiao4*, Yan 6 
Li5*, Bing Liu1,2,3* 7 
 8  1Department  of  Infectious  Diseases,  The  First  Affiliated  Hospital  of  Xi'an  Jiaotong  University,  Xi'an 
Jiaotong University, Shaanxi, 710061, China. 2Key Laboratory of Surgical Critical Care and Life Support, BioBank, Department of Cardiology, 9  Department of Laboratory Medicine, he First Affiliated Hospital of Xi'an Jiaotong University, Shaanxi, 10 
710061, China. 11  3Department of Life Sciences, Faculty of Natural Sciences, Imperial College London, SW7 2AZ London, 
United Kingdom. 4Laboratory of Health Intelligence, Huawei Cloud Computing Technologies Co., Ltd, Guizhou, 550025, 12  China 13  5Department of Pathogen Biology, School of Basic Medicine, State Key Laboratory for Diagnosis and 14 
Treatment of Severe Zoonotic Infectious Diseases, Tongji Medical College, Huazhong University of 15  Science and Technology, Wuhan, 430030, China 16  6College of Life Science and Technology, Beijing University of Chemical Technology, Beijing, China 17  7Key Laboratory of Virology and Biosafety, Wuhan Institute of Virology, Chinese Academy of Sciences, 18  Wuhan, 430071, China. 19  8School of Life Science and health, University of Health and Rehabilitation Sciences, Qingdao, 266113 20   21   22  #These authors contributed equally 23  *Corresponding authors   24 
Abstract 25 
Finding novel compounds and new targets is crucial for antibiotic development. The highly 26 
conserved nucleoid-associated protein (NAP) HU plays a vital role in DNA metabolism and 27 
is indispensable for many bacteria. It also plays crucial roles in biofilm formation and DNA 28 
supercoiling, making it a promising target for antibiotic development. In this work, we con-29 
ducted a structure-based drug screening and identified a group of cinnamic-hydroxamic-acid 30 
derivatives (CHADs) as HU inhibitors. By disrupting the HU-DNA interaction, CHADs in-31 
duce nucleoid deformation, thereby preventing bacterial division and inhibiting growth. Ad-32 
ditionally, they exhibit anti-biofilm activity and supercoiling relaxation properties, which are 33 
crucial for counteracting bacterial stress responses to antibiotics. We demonstrated their anti-34 
bacterial efficacy, synergistic effects with other antibiotics, and effectiveness in treating in-35 
fections in mouse models. Thus, we propose that CHADs represent a new class of potential 36 
antibiotics that could inhibit the bacterial stress response by co-targeting biofilm and super-37 
coiling.
71
Introduction  41 
Antimicrobial resistance (AMR) is a major threat to human health globally (1). The rise of 42 
AMR has been attributed to the overuse of existing antibiotics and the slow 43 
commercialization of new drugs (2-5). Antibiotics combat bacteria through three main 44 
mechanisms: disrupting the synthesis of nucleic acids, the cell wall, or proteins by targeting 45 
key enzymes in these pathways (6). To combat AMR, extensive efforts have been made to 46 
identify new drug targets and develop novel therapeutic strategies (7-9). Among newly 47 
identified targets, HU, a NAP, plays critical roles in bacterial survival, growth, SOS response, 48 
adaptive mutation, cell division, biofilm formation and many other cell processes (10, 11). 49 
HU is encoded by hup gene(s) and is essential for many bacteria (12), while hup deletion in 50 
other bacteria including Escherichia coli (E. coli) causes major growth defects (13).  Small 51 
molecule HU inhibitors have been developed and verified at bacterial level. Targeting either 52 
the “pit” or the a-helical region of the HUs, trans-stilbene derivatives (SDs) and bisphenol 53 
derivatives of fluorene (BDFs) have been developed to intervene the DNA binding properties 54 
of their target HUs. Based on the docked models, SDs have been suggested to break up the 55 
interaction between the basic residues in the pit and DNA in Mycobacterium tuberculosis (M. 56 
tuberculosis) (14) and the African swine fever virus (15). In contrast, BDFs bind to the a-57 
helical region and interfere with the DNA binding “arm” and “pit” allosterically, and this 58 
class of compounds has been shown to be effective against Spiroplasma melliferum (S. 59 
melliferum) (16). Interestingly, Bacillus phage SPO1 is also known to produce a cross-species 60 
HU inhibitor, Gp46 (17). Although the inhibition mechanism of Gp46 differs from those of 61 
SDs and BDFs, as Gp46 does not bind HU via the proposed “pit” or α-helical region, the 62 
existence of a phage HU inhibitor suggests that inhibiting HU would also facilitate phage-63 
mediated bacterial killing. 64 
 65 
interaction for the hits from the ZINC20 library, Belinostat (Fig. 1A), an FDA-approved drug 132 
for treating hematological malignancies and solid tumors, showed an interaction with SaHU 133 
in the WaterLOGSY experiment (Fig. 1B). Further NMR experiments suggest that Belinostat 134 
interacts with the HU proteins of another 5 different bacteria, including A. baumannii, S. 135 
pneumoniae, B. subtilis, M. tuberculosis and S. pyogenes (Fig. S2A).  The binding affinity 136 
(KD) for Belinostat and SaHU was determined at 4.24 ± 0.24 μM (using 1:1 fitting model) 137 
using MicroScale Thermophoresis (MST) (Fig. 1C). The high salt buffer (500 mM NaCl) 138 
used in MST to reduce the capillary retention could potentially affect the electrostatic 139 
interactions between Belinostat and SaHU, which may result in reduced affinity. The KD is 140 
however comparable to the HU inhibitor SD1 but weaker than SD4, whose binding affinities 141 
to HU (M. tuberculosis) are 1.3 ± 0.2 μM and 0.098 ± 0.013 μM, respectively (14). To check 142 
if Belinostat is a SaHU inhibitor that disrupts the SaHU-DNA interaction in vitro, we 143 
performed an electromobility shift assay (EMSA). The result shows that the anti-cancer drug 144 
was able to displace double-stranded DNA (dsDNA) from SaHU (Fig. 1D). Using antibiotic 145 
susceptibility testing (AST), we assessed and confirmed the antimicrobial activity of 146 
Belinostat against S. aureus (ATCC 29213 if not stated otherwise). Following the protocols 147 
and parameters set by CLSI standards (41), we determined the average minimal inhibitory 148 
concentrations (MICs) for the laboratory strain and nine other clinically isolated MRSA (Fig. 149 
1E) to be 364 μg/mL (1.14 mM), which is comparable to both SD1 and SD4, at 400 and 800 150 
μM, respectively. Furthermore, we showed that Belinostat also inhibits the growth of the 151 
Gram-positive model bacterium B. subtilis and the MICs for the two strains (ATCC 6051 and 152 
168) were ~360 μg/mL (~1.13 mM) (Fig. S2B), but has little inhibitory effect against 153 
Pseudomonas aeruginosa (P. aeruginosa, PAO1 if not stated otherwise) (Fig. S2C). This 154 
observation aligns with other HU inhibitors, as the functions of HU can be compensated in 155 
bacteria like E. coli and P. aeruginosa. 156 
Panobinostat, which showed moderate neutrophil infiltration and alveolar wall thickening, 307 
indicative of lung injury (Fig. 5A and S12A). Furthermore, significant reductions in white 308 
blood cells (WBCs), neutrophils (Neu), lymphocytes (Lym) and platelets (PLT), were found 309 
in the Panobinostat-treated group compared to the control, which is consistent with the 310 
reported side effects of Panobinostat (49). There were no observable differences in the 311 
number of red blood cells (RBCs) or haemoglobin (HGB) levels among the three drug groups 312 
(Fig. S12B). These results support the fact that Belinostat is safe for intravenous injection and 313 
Panobinostat is unsuitable for intravenous injection, as well as show that R4Cl has similar 314 
pharmacological efficacy to Belinostat. However, further studies are needed to fully assess 315 
the pharmacokinetic characteristics of R4Cl. 316 
 317 
 318 
CHADs are effective in treating S. aureus infections in both skin infection and septic 319 
mice models 320 
We next tested the CHADs in direct comparison with Fusidic acid (FA) in a skin infection 321 
model. Superficial wounds on the back of mice were infected with S. aureus and treated with 322 
FA or Belinostat. Compared to the control mice, the bacterial content per gram of lesion skin 323 
(CFU/g) were significantly reduced after treatment with FA (2%) or concentrations of 324 
Belinostat between 3 ng/mL (0.01 μM) and 300 ng/mL (1 μM), which is notably smaller than 325 
measured MIC (Fig. 5B). Consistent with these observations, the control group showed 326 
severe lesion in epidermis layer and inflammatory cell infiltration in subcutaneous tissue, but 327 
FA or Belinostat treated groups led to restored epidermis and reduced inflammation (Fig. 328 
5C). We extended the comparison to include three more CHADs (0.1 μM), including 329 

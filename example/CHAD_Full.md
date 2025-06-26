# AI-Guided Discovery of a Phage-Inspired Antibiotic Class with Anti-Biofilm and DNA Supercoiling Relaxation Activities

**Huan Chen**1,2#, **Yingqi Xu**3#, **Zhaoping Xiong**4#, **Hongliang Wang**1#, **Xin Wang**1,2,, **Yue Kang**1,2,, **Zhonglin Wang**2,, **Xiaoyan Zeng**2, **Yahui Liu**5, **Yehuan Zheng**1,2, **Wei Chen**1,2, **Mengzhe Li**6, **Zhenyue Hu**1,2, **Chi Xu**4, **Yue Wu**2, **Yawen Wang**1,2, **Zuyi Yuan**2, **Shuai Yuan**7, **Huadong Liu**8, **Steve Matthews**3*, **Nan Qiao**4*, **Yan Li**5*, **Bing Liu**1,2,3*

---

1. Department of Infectious Diseases, The First Affiliated Hospital of Xi'an Jiaotong University, Xi'an Jiaotong University, Shaanxi, 710061, China.
2. Key Laboratory of Surgical Critical Care and Life Support, BioBank, Department of Cardiology, Department of Laboratory Medicine, the First Affiliated Hospital of Xi'an Jiaotong University, Shaanxi, 710061, China.
3. Department of Life Sciences, Faculty of Natural Sciences, Imperial College London, SW7 2AZ London, United Kingdom.
4. Laboratory of Health Intelligence, Huawei Cloud Computing Technologies Co., Ltd, Guizhou, 550025, China
5. Department of Pathogen Biology, School of Basic Medicine, State Key Laboratory for Diagnosis and Treatment of Severe Zoonotic Infectious Diseases, Tongji Medical College, Huazhong University of Science and Technology, Wuhan, 430030, China
6. College of Life Science and Technology, Beijing University of Chemical Technology, Beijing, China
7. Key Laboratory of Virology and Biosafety, Wuhan Institute of Virology, Chinese Academy of Sciences, Wuhan, 430071, China.
8. School of Life Science and Health, University of Health and Rehabilitation Sciences, Qingdao, 266113

---

\*These authors contributed equally  
\#Corresponding authors

# Abstract

Finding novel compounds and new targets is crucial for antibiotic development. The highly conserved nucleoid-associated protein (NAP) HU plays a vital role in DNA metabolism and is indispensable for many bacteria. It also plays crucial roles in biofilm formation and DNA supercoiling, making it a promising target for antibiotic development. 

In this work, we conducted a structure-based drug screening and identified a group of cinnamic-hydroxamic-acid derivatives (CHADs) as HU inhibitors. By disrupting the HU-DNA interaction, CHADs induce nucleoid deformation, thereby preventing bacterial division and inhibiting growth. Additionally, they exhibit anti-biofilm activity and supercoiling relaxation properties, which are crucial for counteracting bacterial stress responses to antibiotics. 

We demonstrated their antibacterial efficacy, synergistic effects with other antibiotics, and effectiveness in treating infections in mouse models. Thus, we propose that CHADs represent a new class of potential antibiotics that could inhibit the bacterial stress response by co-targeting biofilm and supercoiling.

# Introduction

Antimicrobial resistance (AMR) is a major threat to human health globally. The rise of AMR has been attributed to the overuse of existing antibiotics and the slow commercialization of new drugs. Antibiotics combat bacteria through three main mechanisms: disrupting the synthesis of nucleic acids, the cell wall, or proteins by targeting key enzymes in these pathways. To combat AMR, extensive efforts have been made to identify new drug targets and develop novel therapeutic strategies. Among newly identified targets, HU, a NAP, plays critical roles in bacterial survival, growth, SOS response, adaptive mutation, cell division, biofilm formation and many other cell processes. HU is encoded by hup gene(s) and is essential for many bacteria, while hup deletion in other bacteria including Escherichia coli (E. coli) causes major growth defects. Small molecule HU inhibitors have been developed and verified at bacterial level. Targeting either the “pit” or the a-helical region of the HUs, trans-stilbene derivatives (SDs) and bisphenol derivatives of fluorene (BDFs) have been developed to intervene the DNA binding properties of their target HUs. Based on the docked models, SDs have been suggested to break up the interaction between the basic residues in the pit and DNA in Mycobacterium tuberculosis (M. tuberculosis) and the African swine fever virus. In contrast, BDFs bind to the a-helical region and interfere with the DNA binding “arm” and “pit” allosterically, and this class of compounds has been shown to be effective against Spiroplasma melliferum. Interestingly, Bacillus phage SPO1 is also known to produce a cross-species HU inhibitor, Gp46. Although the inhibition mechanism of Gp46 differs from those of SDs and BDFs, as Gp46 does not bind HU via the proposed “pit” or α-helical region, the existence of a phage HU inhibitor suggests that inhibiting HU would also facilitate phage-mediated bacterial killing.

# Notably, HU is not only indispensable for cell viability in many bacteria but also plays critical roles in biofilm formation and the regulation of DNA supercoiling, both of which are crucial for bacterial stress responses to antibiotics (18-22). Biofilms provide a protective environment that significantly enhances bacterial survival against antibiotics and the host immune system (23). They consist of extracellular polymeric substances (EPS), including polysaccharides (LPS), extracellular DNA (eDNA), and proteins (24). Importantly, HU has been shown to play a crucial role in biofilm formation by binding to eDNA and LPS, acting as a molecular glue (25). Meanwhile, the bacterial supercoiling results from the combined effects of transcription, replication, topoisomerase activity, and NAPs including HU (26). HU can induce and constrain supercoiling by bending and coiling DNA (27-29), and its deletion reduces the supercoiling of both plasmid and chromosomal DNA (30). HU-DNA interaction, likely through its role in adjusting DNA supercoiling, is considered as a general mechanism for bacterial transcriptional regulation during the cell cycle and stress responding including antibiotics (20, 31). Since both biofilm formation and supercoiling are important for bacterial antibiotic resistance, a HU inhibitor with anti-biofilm and anti-supercoiling properties could counteract bacterial stress responses to antibiotics, in addition to exerting its own antibacterial activity. However, the potential anti-biofilm and anti-supercoiling effects of the pioneering compounds, BDFs and SDs, have yet to be described. 

# Inspired by the cross-species nature of the phage HU inhibitor Gp46, we conducted a structure-based drug screening using the two HU major binding sites of phage protein, which led to the identification of a group of HU inhibitors can be classified as CHADs. This group of small molecules includes commercialized anti-cancer drugs Belinostat (trade name Beleodaq, also known as PXD101) (32) and Panobinostat (trade name Fardak) (33), investigational drugs Dacinostat (LAQ824) (34) and Parcinostat (SB939) and other

CHADs that share the same functional group. We demonstrate that CHADs target the highly conserved regions of HU proteins and displace DNA from HUs in vitro. They inhibit bacterial growth by causing a phenotype similar to that of Gp46 overexpression, i.e., an elongated cell shape in the bacilli, inheriting the property of their phage protein template. In Staphylococcus aureus (S. aureus), it causes nucleoid loss in the cocci, different from the phenotype in Bacillus subtilis (B. subtilis) and that of FtsZ inhibitors. They are effective against the laboratory strains and clinically separated multidrug-resistant bacteria strains, including 50 clinically isolated methicillin-resistant S. aureus (MRSA) strains, M. tuberculosis including H37Rv and an extensively drug-resistant tuberculosis (XDR-TB) strain, and Acinetobacter baumannii (A. baumannii). Due to the roles of HU in biofilm formation and supercoiling, these HU inhibitors also benefit from their anti-biofilm and supercoiling relaxation properties. With their cytotoxicity and antibacterial activity verified in the in vivo animal models, CHADs have the potential to be used as stand-alone antibiotics or as adjuvants with other antibiotics.

# Results

Phage-inspired and structure-based screening for HU inhibitors

Targeting either the “pit” or the α-helical region of the HUs, SDs and BDFs have been developed to intervene the DNA binding properties of their target HUs (Fig. S1A-S1C). However, SPO1 phage protein Gp46 binds to *B. subtilis* HU (HBsu) via two major interfaces - the edge of the pit, i.e., the outermost β sheets (site 1), and the hydrophobic patches (site 2) on two arms (Fig. S1D), different from SDs and BDFs. To identify the most conserved residues in the two sites for development of broad-range inhibitors, we performed multi-sequence alignment with *B. subtilis*, *S. aureus*, *M. tuberculosis*, *Streptococcus pneumoniae* (*S. pneumoniae*), *Streptococcus pyogenes* (*S. pyogenes*) and *A. baumannii* representing bacterial pathogens which have homodimeric HUs (Fig. S1E). In site 1, most residues (shown for the HBsu) are highly conserved and in site 2, the hydrophobic and charged residues are highly conserved, which include R58, R61 and I71. Using these two interfaces for targeting site selection, we first virtually screened compound libraries originating from DrugBank (37) and ZINC20 (38) using AutoDock Vina (39) (Table S1-S4). In addition, compound protein interaction (CPI) (40) score was also used along with the virtual docking to rank the DrugBank molecules (Table S1 and S2). The docking results suggest that most highly ranked molecules occupy the key sites (Fig. S1F-S1H). In site 1, most molecules interact with G46 and K80 which are highly conserved across species. In site 2, all molecules dock with hydrophobic patch anchored on the highly conserved I71.

Belinostat is a HU inhibitor and causes nucleoid deformation in *B. subtilis* and *S. aureus*

Using ligand-observed nuclear magnetic resonance (NMR) Water ligand observed gradient spectroscopy (WaterLOGSY) experiments, we tested interactions between top candidates from each screen and the *S. aureus* HU protein (SaHU). While there was no observed

## Interaction of Belinostat with SaHU Protein

Belinostat, an FDA-approved drug for treating hematological malignancies and solid tumors, showed interaction with SaHU in the WaterLOGSY experiment. Further NMR experiments suggest that Belinostat interacts with HU proteins of five different bacteria: A. baumannii, S. pneumoniae, B. subtilis, M. tuberculosis, and S. pyogenes.

### Binding Affinity Determination

The binding affinity (KD) for Belinostat and SaHU was determined to be 4.24 ± 0.24 µM using MicroScale Thermophoresis (MST). The high salt buffer (500 mM NaCl) used in MST could potentially affect the electrostatic interactions between Belinostat and SaHU.

### Inhibition of SaHU-DNA Interaction

Belinostat was found to displace double-stranded DNA (dsDNA) from SaHU, suggesting its inhibitory effect on the SaHU-DNA interaction in vitro.

### Antimicrobial Activity

- **S. aureus**: Belinostat exhibited antimicrobial activity against S. aureus with an average minimal inhibitory concentration (MIC) of 364 µg/mL (1.14 mM).
- **B. subtilis**: The MIC for B. subtilis strains was ~360 µg/mL (~1.13 mM).
- **P. aeruginosa**: Belinostat had little inhibitory effect on P. aeruginosa.

These findings suggest that Belinostat acts as an inhibitor of SaHU and shows antimicrobial activity against certain bacteria strains.

### Overexpression of Gp46 in B. subtilis
Overexpressing Gp46 in its native host B. subtilis causes cell elongation and nucleoid deformation (17). To check if the effects of Belinostat are similar, we examined the phenotypes of B. subtilis (strain 168) and S. aureus that were treated with 400 µg/mL (1.26 mM) of Belinostat. Belinostat-treated B. subtilis cells showed diffused nucleoid structures and elongated body shapes in both Gram staining and transmission electron microscopy (TEM) observations, resembling the phenotype caused by overexpression of Gp46 (Fig. 1F). For Belinostat-treated S. aureus, there was no noticeable difference in Gram staining, however, TEM revealed that Belinostat-treated S. aureus showed a deformed nucleoid structure (Fig. 1G). These observations suggest that the inhibition of bacterial HU is a major contributor to the antibacterial activity of Belinostat.

### Identification of CHADs as a Class of Antibacterial Compounds
We next questioned whether the identification of Belinostat as an anti-bacterial agent was an isolated case or could the functional group responsible for its anti-microbial activity serve as the scaffold for optimization. Reports in the literature indicate that histone deacetylase inhibitors (HDACi) may be effective in treating bacterial infections by modulating human defense systems (42-44). This suggests that the hydroxamic acid (HA) or cinnamic hydroxamic acid (CHA) groups, shared by these non-selective HDACis, could contribute to their antimicrobial activity. We used the Huawei Deep-learning based PANGU Molecule Optimizer (PGMO) in an attempt to expand our lead compound library (40). By choosing the different functional groups as scaffolds, we generated a collection of derivatives of Belinostat (Table S5A and S5B). Although the results of PGMO did not contain any commercialized drugs, some of the top optimized small molecules possess cinnamic hydroxamic acid (CHA) group which resemble another FDA-approved drug Panobinostat, which is also a HDACi.

(Fig. 2A and S3A). Importantly, both Panobinostat and Belinostat are also CHADs. We next showed that Panobinostat also possesses antimicrobial activity and determined the MIC for S. aureus to be 150 µg/mL (430 µM) (Fig. S3B). To determine if CHA group is essential for the antimicrobial activity, we selected another HDACi, Vorinostat (trade name Zolinza and Fig. 2B) (45), which only has the HA group, and demonstrated that it did not interact with SaHU nor inhibit the growth of S. aureus (Fig. S3C, S3D and S3E). Furthermore, two further HDAC inhibitors, Dacinostat (34) and Parcinostat (35), also showed antibacterial activity against S. aureus (Fig. 2C and S3C). In summary, the CHA group is likely to be the key functional group responsible for the antimicrobial activity of HDAC inhibitors.

To confirm whether CHA is responsible for the anti-bacterial properties, we defined the CHA group as the scaffold base and searched ZINC20 for its derivatives. A collection of small molecules that contains the CHA group was identified (Figure 2D, 2E, S4A and S4B). Two molecules that contain one or two chlorine atoms as the R group of CHA, termed R4Cl and R24Cl respectively, showed antibacterial properties in the AST (Fig. 2D and S4A). We then determined the MICs of R4Cl and R24Cl for S. aureus, both to be approximately 30 µg/mL (152 µM of R4Cl and 130 µM of R24Cl) (Fig. S4B). Compared with Belinostat or Panobinostat, R4Cl and R24Cl have significant lower MICs, suggesting the chlorine substitution at the R4 position of the CHA scaffold has an important role in the antimicrobial properties. To examine the role of the R4 chlorine, we synthesized two molecules that have the halogen substitutions, namely R4F and R4Br (Fig. 2E). Interestingly, R4F partially inhibited the growth of S. aureus at 150 µg/mL (828 µM) and R4Br has a higher MIC than R4Cl, at 60 µg/mL (248 µM) (Fig. S4A and S4C). MST experiments to determine the affinities between R4 substitutes and SaHU had large errors, suggesting that the high salt may interfere the interaction. Furthermore, CHA, without any R4 substitution, also showed.

## Antibacterial Mechanism of CHADs

The antibacterial ability of CHADs was investigated, showing partial inhibition of the growth of *S. aureus* at 200 µg/mL. The binding affinity to SaHU was determined to be 5.77 ± 0.93 µM, similar to that of Belinostat. The importance of the R4 group for the antibacterial properties of CHADs was highlighted. A list of proposed CHADs with potential antibacterial activities was provided. Additionally, the role of the HA group in antibacterial activity was explored, with cinnamic acid showing a loss of antibacterial activity compared to CHA.

### CHADs Target Site 1 of SaHU

Structural studies were conducted to elucidate the antibacterial mechanism of CHADs at a molecular level. Although attempts to crystallize the complex failed, a crystal structure of apo SaHU at 2.14 Å was obtained. A mutant SaHUD15G was constructed to stabilize the protein in solution, and NMR studies were performed. Significant peak broadening was observed in the 1H-15N HSQC spectrum of 15N-labeled SaHUD15G upon the addition of Panobinostat. The changes in peak intensity were plotted against residue number, with perturbations mostly observed in site 1.

# Binding Mechanism of R4Cl to SaHUD15G

In the study, it was observed that R4Cl binds to site 1 of SaHUD15G, similar to the binding observed in virtual screening. This interaction was characterized by peak broadening of surrounding residues. Additionally, chemical shift perturbations were observed in the NMR titration experiment of CHA, indicating a weaker interaction.

By combining the active interfacial residues of SaHUD15G from NMR titration and the CHA group from R4Cl, a R4Cl-SaHUD15G complex was calculated using the High Ambiguity Driven protein-protein Docking Server (HADDOCK). The model showed that the CHAD positions at site 1 of SaHUD15G with the HA group forming multiple hydrogen bonds with surrounding residues. The ring of R4Cl interacts with specific amino acid donors and side chains, effectively blocking the HU-DNA interaction at site 1 of HU.

Molecular dynamics (MD) simulations were employed to evaluate the free energy calculation for the SaHUD15G-R4Cl complex, indicating a stable binding interaction between R4Cl and SaHUD15G.

The study further emphasized that any additional substituents on the ring of R4Cl that extend towards the pit region of HU would interfere with the HU-DNA interaction, potentially affecting the efficacy of the drug. This finding highlights the importance of understanding the binding mechanism of R4Cl to SaHUD15G in modulating the HU-DNA interaction.

## Binding Site Analysis
During the simulation, a consistent binding site was observed with an absolute binding free energy of 13.36 kcal/mol (Supplementary Video 1). Analysis of energy contribution per residue indicates that residues L44, I45, G46, K80, G82, and K83 play a significant role in the binding free energy (Fig. S8A and S8B). Furthermore, the relative binding free energy (RBFE, ΔΔG) was calculated for all MIC-determined molecules shown in Fig. 2 using the SaHUD15G-R4Cl model with Belinostat as the reference compound. A positive correlation was observed between the experimentally determined MICs of these molecules and the calculated ΔΔG, with Panobinostat as the only outlier (Fig. S8C). The agreement between MD-based calculations and experimental MICs suggests that the NMR-derived mode of the complex could be valuable for further optimization of the CHADs.

## Antibacterial Property of CHADs
To assess the effectiveness of CHADs against drug-resistant bacterial strains, Panobinostat from the commercialized drug group and R4Cl from the new molecule group were selected. Panobinostat and R4Cl were tested on 50 clinically isolated MRSA strains and two strains of M. tuberculosis. Fifty MRSA strains were isolated from local hospitals (the multidrug-resistant profile can be found in Fig. S9A), and their evolutionary relationship was analyzed, showing no identical strains (Fig. S9B). The average MIC of Panobinostat against the 50 MRSA strains was 157 µg/mL (449 µM) (Fig. 4A, upper), while R4Cl exhibited an average MIC of 30 µg/mL (152 µM) (Fig. 4A, lower), significantly lower than Panobinostat. The resazurin microtiter plate assay indicated that R4Cl effectively inhibited the growth of both M. tuberculosis (H37Rv unless stated otherwise) and an XDR-MTB strain (multidrug-resistant profile in Table S7), with MICs for XDR-TB and M. tuberculosis at 10 and 12 µg/mL (51 and 61 µM) (Fig. 4B). Similarly, the MIC values determined for...

# Antibacterial Potential of CHADs

The minimum inhibitory concentration (MIC) of R4Cl for *A. baumannii* (BBA-1605 unless stated otherwise) is around 12 µg/mL (61 µM) (Fig. 4C). Additionally, the frequency of resistance (FoR) to R4Cl was found to be 1 × 10^-10 for *S. aureus*. Given that HU plays active roles in bacterial supercoiling and biofilm formation, both of which contribute to bacterial resistance, its inhibitors would potentially have the advantage of a low FoR.

## Toxicity tests and animal models

To demonstrate the potential of CHADs in antibacterial applications, two commercial anti-cancer drugs, Belinostat and Panobinostat, along with the new molecule R4Cl, were selected for safety evaluations in mice. For skin applications, the three drugs were applied to the skin of mice for seven consecutive days at a concentration of 1000 mg/kg. No morphological abnormalities were observed in the heart, liver, kidney, lung, or spleen tissues in any of the drug-treated groups compared to the control (Fig. S10).

For intravenous injection, the median lethal dose (LD50) was determined using the up-and-down procedure to assess acute toxicity. The LD50 values for Belinostat and R4Cl were both determined to be 242.7 mg/kg. However, Panobinostat, which is only approved for oral administration, has a lower LD50 of 78.64 mg/kg (Fig. S11 A-C). These LD50 values suggest that R4Cl has a similar toxicity level to Belinostat. Additionally, the three drugs were subjected to toxicity tests in mice for seven consecutive days via daily intravenous injections. Belinostat and R4Cl were administered at a daily dose of 44 mg/kg, while Panobinostat was given at 28 mg/kg due to its higher toxicity. After 7 days, the mice were sacrificed. Blood, heart, liver, kidney, lung, and spleen tissues were harvested, and tissue sections were stained with hematoxylin-eosin (H&E) for histopathological assessment. No morphological abnormalities were observed, except for the lung tissues treated with Belinostat.

# Results

Panobinostat, which showed moderate neutrophil infiltration and alveolar wall thickening, indicative of lung injury (Fig. 5A and S12A). Furthermore, significant reductions in white blood cells (WBCs), neutrophils (Neu), lymphocytes (Lym) and platelets (PLT), were found in the Panobinostat-treated group compared to the control, which is consistent with the reported side effects of Panobinostat (49). There were no observable differences in the number of red blood cells (RBCs) or hemoglobin (HGB) levels among the three drug groups (Fig. S12B). These results support the fact that Belinostat is safe for intravenous injection and Panobinostat is unsuitable for intravenous injection, as well as show that R4Cl has similar pharmacological efficacy to Belinostat. However, further studies are needed to fully assess the pharmacokinetic characteristics of R4Cl.

CHADs are effective in treating S. aureus infections in both skin infection and septic mice models

We next tested the CHADs in direct comparison with Fusidic acid (FA) in a skin infection model. Superficial wounds on the back of mice were infected with S. aureus and treated with FA or Belinostat. Compared to the control mice, the bacterial content per gram of lesion skin (CFU/g) were significantly reduced after treatment with FA (2%) or concentrations of Belinostat between 3 ng/mL (0.01 µM) and 300 ng/mL (1 µM), which is notably smaller than measured MIC (Fig. 5B). Consistent with these observations, the control group showed severe lesion in epidermis layer and inflammatory cell infiltration in subcutaneous tissue, but FA or Belinostat treated groups led to restored epidermis and reduced inflammation (Fig. 5C). We extended the comparison to include three more CHADs (0.1 µM), including Panobinostat, R4Cl and a HDACi - Vorinostat (also 0.1 µM), in the FA-resistant MRSA infection model. All three CHADs were effective in clearing the infection in the skin lesion.

### Results

Regenerative changes were observed with the use of CHADs, as shown in Fig. 5D and E. However, FA or Vorinostat did not inhibit bacteria propagation and led to intense inflammatory cell infiltration in the subcutaneous tissues. A comparative study showed that CHADs effectively treated superficial infections, while HDACi - Vorinostat without the CHA functional group was unable to suppress the infection and even promoted it. Among the CHADs, R4Cl with the lowest MIC performed the best, while Belinostat with the highest MIC performed the worst in terms of bacteria count (Fig. 5D), demonstrating the antibacterial activities of CHADs in an animal model.

To verify the antiseptic effect of CHADs in a systemic infection, Belinostat was tested in S. aureus- and P. aeruginosa-septic mouse models. Belinostat, approved for intravenous injection to treat peripheral T-cell lymphoma, showed significant rescue effects with a survival rate of up to 90% in S. aureus-treated mice and an extension in survival time in P. aeruginosa-treated mice. This suggests that AST results can be translated into in vivo models, making Belinostat a potential emergency treatment for septic patients with S. aureus infection.

Moreover, the survival assay was repeated using R4Cl at a lower dose of 3 mg/kg due to its lower MIC compared to Belinostat. The reduced dose of R4Cl was able to rescue S. aureus-treated mice, further highlighting its efficacy in treating infections.

### Conclusion

These findings emphasize the effectiveness of CHADs in treating infections, with R4Cl showing promising results in rescuing mice from septic conditions. The translation of AST results into in vivo models suggests the potential use of CHADs as emergency treatments for bacterial infections, particularly S. aureus, in clinical settings.

The anti-biofilm property of CHAD
 
In the AST, HU exists in three forms: cellular, in the growth medium, and in biofilm. This differs from in vivo models, where an environment to confine extracellular free HU, as seen in culture plates, does not exist, and HU primarily remains intracellular. To determine the distribution of HU in these three forms under in vitro conditions, we treated S. aureus with or without R4Cl and analyzed HU levels in each form using mass spectrometry (MS). The results showed that without R4Cl, more HU was found in extracellular forms, i.e., in biofilm and growth medium, than in the cellular form, with the highest HU levels detected in biofilm. When treated with a subinhibitory concentration of R4Cl (0.5 × MIC, 15 µg/mL), the majority of HU remained extracellular; however, the distribution ratio shifted, with the lowest HU levels observed in biofilm. And the microbial counts of the two cultures were almost identical. These results explain the discrepancy between in vivo and in vitro findings. The observation that HU levels increased in both the cell and growth medium but decreased in the biofilm after R4Cl treatment suggests that R4Cl may possess anti-biofilm properties.

# Inhibition of Biofilm Formation by CHADs

To verify if CHADs could inhibit biofilm formation, we tested R4Cl at non-inhibitory concentrations for *P. aeruginosa* (20 µg/mL or 101 µM) to avoid interference from its antibacterial activity. The crystal violet staining results suggest that R4Cl inhibits biofilm formation of *P. aeruginosa* in a dose-dependent manner at concentrations below 20 μg/mL (101 µM) (Fig. 6B). The scanning electron microscopy (SEM) also shows the biofilm formation was inhibited. We then used a biofilm eradication assay to verify the potential biofilm-destructive effect of CHADs using crystal violet staining. We demonstrated that R4Cl has a strong biofilm-destructive effect against by *S. aureus*, with over 60% destruction at 1 × MIC (30 µg/mL or 152 µM) and over 80% at 2 × MIC (60 µg/mL or 304 µM) (Fig. 6C). R4Cl exhibited a similar effect against biofilms formed by *P. aeruginosa*, although it is not effective against the bacterium itself. And the SEM results also support the crystal violet staining data, showing the disruption of biofilms performed by *S. aureus* and *P. aeruginosa*.  

# Supercoiling Relaxation and Antibiotic Synergy Effect of R4Cl

To verify if supercoiling is affected as anticipated, we used biotinylated trimethyl psoralen (bTMP), which preferentially binds to negatively supercoiled DNA, to determine whether CHADs can influence the DNA supercoiling state. Using two model bacteria, *E. coli* (MG1655) and *B. subtilis* (168), we compared their supercoiling level with and without R4Cl treatment. During the exponential phase, the normalized fluorescence intensities (AU per cell) for *E. coli* and *E. coli* treated with R4Cl were 891 and 456, respectively (Fig. 7A). Similarly, the normalized fluorescence intensities for *B. subtilis* and *B. subtilis* treated with R4Cl were 8465 and 3841, respectively (Fig. 7B). The decrease in fluorescence intensity indicates a reduction in supercoiling levels, demonstrating the supercoiling relaxation property of R4Cl. As supercoiling is a master transcriptional regulator for bacteria, relaxed supercoiling level would affect global gene expression. Indeed, transcriptome analysis.

(KEGG enrichment) revealed an enrichment of stress-response genes in the presence of R4Cl, despite the compound not inhibiting E. coli growth at 10 µg/mL or causing morphological changes (Fig. S15A–C).

Since dynamic supercoiling adjustments are crucial for bacterial adaptation to environmental stresses, R4Cl-induced relaxation may impair this regulatory mechanism, preventing bacteria from fine-tuning their supercoiling in response to changing conditions. We then tested whether the relaxed supercoiling state induced by R4Cl could influence the bacterial response to other antibiotics. Using carbenicillin (CB) as an example, the phenotype of R4Cl-treated E. coli was notably different from the control: E. coli cells exhibited a characteristic elongated shape under CB exposure, whereas most R4Cl-treated cells were significantly shorter under the same conditions (Fig. 7C). Furthermore, the MIC of CB decreased from 10 µg/mL to 8 µg/mL in the presence of R4Cl. Subsequent transcriptome analysis revealed altered gene expression patterns in the presence of R4Cl (Fig. 7D, E). Specifically, the two-component system, which enables bacteria to sense and respond to environmental changes, was enriched in R4Cl-treated cells. In contrast, metabolic adaptation to diverse environments was the most enriched pathway in control cells but was notably absent in R4Cl-treated cells. These results show that while bacteria can partially compensate for the loss of supercoiling regulation through the two-component system, this compensation appears to be incomplete, as evidenced by the drop in MIC for CB. Thus, these findings further support that R4Cl can misdirect the optimal bacterial responses to CB by functioning as a HU inhibitor.

Given the established role of supercoiling in bacterial antibiotic resistance (53), we therefore tested the potential antibiotic synergy effect of R4Cl with rifamycin, as antibiotic combinations have become standard therapy for treating tuberculosis (54). The checkerboard assay, based on the resazurin microtiter plate method, clearly demonstrates synergy between.

```markdown
R4Cl and rifamycin. The fractional inhibitory concentration (FIC) index was calculated to be 0.21, indicating a strong interaction between the two drugs (Fig. 7F). Thus, R4Cl could serve as an adjuvant agent as part of combination therapies for tuberculosis due to its synergistic effect with rifamycin. 
```

## Discussion

The application of phages has been extensively explored to compensate for the current situation of antibiotics and tackle multidrug-resistant bacterial infections \[55-57\]. In addition, phage-inspired target discovery exploits phage hijacking strategies to facilitate the development of novel small-molecule antibiotics \[58\]. While bacterial RNA polymerase (RNAP) is arguably one of the most common phage targets, the cell division protein FtsZ, DNA replication protein b-clamp, HU, and glycolysis enzyme enolase are among the diverse targets that phages use to hijack host metabolism \[17, 59-61\]. In this study, we drew inspiration from phage SPO1 protein Gp46 and selected its interfaces with the bacterial HU protein as sites for virtual drug screening. After identifying the initial compound and its key functional group, we expanded our search to develop a lead compound library. Following validation at molecular, bacterial, and animal model levels, we confirmed the antibacterial activity of CHADs. Since the anti-cancer drugs like Belinostat and Panobinostat have been proven safe in clinical trials, repurposing them presents a fast-track and cost-effective approach. Moreover, R4Cl is a promising candidate for further development, as it has improved effectiveness against clinically significant bacterial pathogens, including S. aureus, A. baumannii, and M. tuberculosis.

Biofilm provides a protective environment that significantly enhances bacterial survival against antibiotics. Although biofilm exhibits resistance to antibiotic treatment due to multiple tolerance mechanisms, some antibiotics like macrolides have anti-biofilm properties \[62\]. However, CHADs’ mechanism of action differs from that of macrolides, as it inhibits the synthesis of the proteins responsible for biofilm formation \[63\]. As HU can be released extracellularly and become the so-called molecular glue in the biofilm through the lysis of dead cells, explosive cell lysis, and secretion via the type IV secretion system.


Inhibitors CHADs exhibit both anti-biofilm formation and biofilm eradication capabilities. Consequently, CHADs exhibit strong biofilm eradication effects, making it a promising candidate for the treatment of persistent biofilm-associated infections.

DNA supercoiling occurs naturally during cellular processes such as DNA replication and transcription, and its balance is controlled antagonistically by DNA gyrase and topoisomerase I. Bacterial topoisomerase inhibitors, such as quinolones, constitute a class of antibiotics that target DNA gyrase and topoisomerase IV, inhibiting the DNA breakage and rejoining process essential for DNA/RNA synthesis. NAPs, such as HU, also regulate supercoiling through their interactions with DNA. However, unlike topoisomerases, HU does not introduce DNA breaks. Instead, the HU-DNA interaction is considered a general mechanism for bacterial transcriptional regulation during the cell cycle and stress response. CHADs exhibit a strong supercoiling relaxation effect by disrupting the HU-DNA interaction, thereby interfering with bacterial stress responses to antibiotic exposure. As demonstrated during CB treatment, CHADs altered the expression of genes required for CB tolerance and affected bacterial morphology. Consequently, CHADs can counteract bacterial resistance mechanisms by relaxing DNA supercoiling and altering the stress response to enhance the efficacy of antibiotics.

The additional anti-biofilm and anti-supercoiling effects make CHAD a rather unique candidate for further development as a stand-alone antibiotic. Likely due to the combination of these counteracting effects against bacterial stress responses, CHADs exhibit a low frequency of resistance and a strong synergistic effect when used with other antibiotics. Notably, its synergy with rifamycin may provide new therapeutic options for treating tuberculosis, making it a potential adjuvant to enhance the efficacy of other antibiotic treatments.

## Data Availability

- The structural coordinate of SaHU has been deposited in Protein Data Bank under accession code 8HD5.
- The sequencing data for the 50 MRSA strains is available under BioProject number SUB14217833.
- The RNA-seq data are available in the SRA under accession number PRJNA1227296.

## Acknowledgments

This project is supported by:
- The National Key R&D Program of China (2021YFA1301201)
- The National Natural Science Foundation of China (32270151)
- Key research and development plan of Shaanxi Province (2021ZDLSF01-10)

Special thanks to Dr. Denghui Liu, Dr. Peipei Zhang, and Miss Hejia Dong for useful discussions.

## Author Contributions

- B.L. conceived the study and designed experiments
- H.C. prepared the samples, performed the docking, biochemical, cellular, and animal experiments
- Y.X. performed NMR analysis
- Z.X. performed the AI work and molecular dynamics
- X.W. performed the works on Belinostat
- Y.K. performed the animal work
- Z.W. determined the MICs
- Y.L. performed the crystallography-related work and structure-based inhibitor screening
- W.C. purified the HU proteins and performed WaterLOGSY experiments
- M.L. performed full genome sequencing and analyzed the data
- X.Z. contributed the clinically isolated bacterial strains
- B.L. analyzed the data from all authors and wrote the first draft
- B.L. revised the manuscript with input from all authors.

# References

1. J. O'Neill, "Tackling drug-resistant infections globally: final report and recommendations." (2016).

2. B. Aslam et al., "Antibiotic resistance: a rundown of a global crisis." Infect Drug Resist 11, 1645-1658 (2018).

3. L. L. Silver, "Challenges of antibacterial discovery." Clin Microbiol Rev 24, 71-109 (2011).

4. P. S. Hoffman, "Antibacterial Discovery: 21st Century Challenges." Antibiotics (Basel) 9, (2020).

5. D. Goel, "Bedaquiline: A novel drug to combat multiple drug-resistant tuberculosis." J Pharmacol Pharmacother 5, 76-78 (2014).

6. M. A. Kohanski, D. J. Dwyer, J. J. Collins, "How antibiotics kill bacteria: from targets to networks." Nature Reviews Microbiology 8, 423-435 (2010).

7. E. M. Hart et al., "A small-molecule inhibitor of BamA impervious to efflux and the outer membrane permeability barrier." Proceedings of the National Academy of Sciences of the United States of America 116, 21748-21757 (2019).

8. A. Luther et al., "Chimeric peptidomimetic antibiotics against Gram-negative bacteria." Nature 576, 452-+ (2019).

9. N. P. Bullen et al., "An ADP-ribosyltransferase toxin kills bacterial cells by modifying structured non-coding RNAs." Mol Cell, (2022).

10. P. Stojkova, P. Spidlova, J. Stulik, "Nucleoid-Associated Protein HU: A Lilliputian in Gene Regulation of Bacterial Virulence." Front Cell Infect Microbiol 9, 159 (2019).

11. A. B. Williams, P. L. Foster, "The Escherichia coli histone-like protein HU has a role in stationary phase adaptive mutation." Genetics 177, 723-735 (2007).

12. S. Fernandez, F. Rojo, J. C. Alonso, "The Bacillus subtilis chromatin-associated protein Hbsu is involved in DNA repair and recombination." Molecular Microbiology 23, 1169-1179 (1997).

13. A. M. Dri, J. Rouviereyaniv, P. L. Moreau, "Inhibition of Cell-Division in Hupa Hupb Mutant Bacteria Lacking Hu Protein." Journal of Bacteriology 173, 2852-2863 (1991).

14. T. Bhowmick et al., "Targeting Mycobacterium tuberculosis nucleoid-associated protein HU with structure-based inhibitors." Nature Communications 5, (2014).

15. R. Liu et al., "The structural basis of African swine fever virus pA104R binding to DNA and its inhibition by stilbene derivatives." Proc Natl Acad Sci U S A 117, 11000-11009 (2020).

16. Y. K. Agapova et al., "Structure-based inhibitors targeting the alpha-helical domain of the Spiroplasma melliferum histone-like HU protein." Scientific Reports 10, (2020).

17. P. P. Zhang et al., "Bacteriophage protein Gp46 is a cross-species inhibitor of nucleoid-associated HU proteins." Proceedings of the National Academy of Sciences of the United States of America 119, (2022).

18. M. Hammel, "HU multimerization shift controls nucleoid compaction." Acta Crystallographica a-Foundation and Advances 73, C296-C296 (2017).

19. B. Thakur, K. Arora, A. Gupta, P. Guptasarma, "The DNA-binding protein HU is a molecular glue that attaches bacteria to extracellular DNA in biofilms." Journal of Biological Chemistry 296, (2021).

20. S. G. Remesh et al., "Nucleoid remodeling during environmental adaptation is regulated by HU-dependent DNA bundling." Nat Commun 11, 2905 (2020).

21. H. Tanaka et al., "Role of HU proteins in forming and constraining supercoils of chromosomal DNA in Escherichia coli." Mol Gen Genet 248, 518-526 (1995).

22. M. A. Webber et al., "Clinically relevant mutant DNA gyrase alters supercoiling, changes the transcriptome, and confers multidrug resistance." mBio 4, (2013).

## References

1. H. C. Flemming et al., "Biofilms: an emergent form of bacterial life." *Nat Rev Microbiol* 14, 563-575 (2016).
   
2. D. Sharma, L. Misba, A. U. Khan, "Antibiotics versus biofilm: an emerging battleground in microbial communities." *Antimicrob Resist Infect Control* 8, 76 (2019).
   
3. B. Thakur, K. Arora, A. Gupta, P. Guptasarma, "The DNA-binding protein HU is a molecular glue that attaches bacteria to extracellular DNA in biofilms." *J Biol Chem* 296, 100532 (2021).
   
4. A. Lal et al., "Genome scale patterns of supercoiling in a bacterial chromosome." *Nat Commun* 7, 11055 (2016).
   
5. F. Guo, S. Adhya, "Spiral structure of Escherichia coli HUalphabeta provides foundation for DNA supercoiling." *Proc Natl Acad Sci U S A* 104, 4309-4314 (2007).
   
6. L. Huang, Z. Zhang, R. McMacken, "Interaction of the Escherichia coli HU Protein with Various Topological Forms of DNA." *Biomolecules* 11 (2021).
   
7. S. S. Broyles, D. E. Pettijohn, "Interaction of the Escherichia coli HU protein with DNA. Evidence for formation of nucleosome-like structures with altered DNA helical pitch." *J Mol Biol* 187, 47-60 (1986).
   
8. M. Malik, A. Bensaid, J. Rouviere-Yaniv, K. Drlica, "Histone-like protein HU and bacterial DNA topology: suppression of an HU deficiency by gyrase mutations." *J Mol Biol* 256, 66-76 (1996).
   
9. K. J. Cheung, V. Badarinarayana, D. W. Selinger, D. Janse, G. M. Church, "A microarray-based antibiotic screen identifies a regulatory role for supercoiling in the osmotic stress response of Escherichia coli." *Genome Res* 13, 206-215 (2003).
   
10. H. Z. Lee et al., "FDA Approval: Belinostat for the Treatment of Patients with Relapsed or Refractory Peripheral T-cell Lymphoma." *Clinical Cancer Research* 21, 2666-2670 (2015).
   
11. L. A. Raedler, "Farydak (Panobinostat): First HDAC Inhibitor Approved for Patients with Relapsed Multiple Myeloma." *Am Health Drug Benefits* 9, 84-87 (2016).
   
12. E. K. Rowinsky et al., "A phase I, pharmacokinetic (PK) and pharmacodynamic (PD) study of a novel histone deacetylase (HDAC) inhibitor LAQ824 in patients with advanced solid tumors." *Journal of Clinical Oncology* 22, 200s-200s (2004).
   
13. V. Novotny-Diermayr et al., "The oral HDAC inhibitor pracinostat (SB939) is efficacious and synergistic with the JAK2 inhibitor pacritinib (SB1518) in preclinical models of AML." *Blood Cancer Journal* 2 (2012).
   
14. S. Tripathy, S. K. Sahu, "FtsZ inhibitors as a new genera of antibacterial agents." *Bioorg Chem* 91, 103169 (2019).
   
15. D. S. Wishart et al., "DrugBank: a comprehensive resource for in silico drug discovery and exploration." *Nucleic Acids Res* 34, D668-672 (2006).
   
16. J. J. Irwin et al., "ZINC20-A Free Ultralarge-Scale Chemical Database for Ligand Discovery." *J Chem Inf Model* 60, 6065-6073 (2020).
   
17. J. Eberhardt, D. Santos-Martins, A. F. Tillack, S. Forli, "AutoDock Vina 1.2.0: New Docking Methods, Expanded Force Field, and Python Bindings." *Journal of Chemical Information and Modeling* 61, 3891-3898 (2021).
   
18. X. Lin et al., "PanGu Drug Model: learn a molecule like a human." *Sci China Life Sci* (2022).
   
19. R. M. Humphries et al., "CLSI Methods Development and Standardization Working Group Best Practices for Evaluation of Antimicrobial Susceptibility Tests." *J Clin Microbiol* 56 (2018).
   
20. L. Schwartz et al., "Repurposing HDAC inhibitors to enhance ribonuclease 4 and 7 expression and reduce urinary tract infection." *Proc Natl Acad Sci U S A* 120, e2213363120 (2023).

### References

1. M. Mombelli et al., Histone deacetylase inhibitors impair antibacterial defenses of macrophages. *J Infect Dis* 204, 1367-1374 (2011). 
   
2. A. M. Grabiec, J. Potempa, Epigenetic regulation in bacterial infections: targeting histone deacetylases. *Crit Rev Microbiol* 44, 336-350 (2018). 
   
3. A. K. Bubna, Vorinostat-An Overview. *Indian J Dermatol* 60, 419 (2015). 
   
4. W. Liu, H. M. Vu, E. P. Geiduschek, D. R. Kearns, Solution structure of a mutant of transcription factor 1: implications for enhanced DNA binding. *J Mol Biol* 302, 821-830 (2000). 
   
5. G. Van Zundert et al., The HADDOCK2.2 web server: user-friendly integrative modeling of biomolecular complexes. *Journal of molecular biology* 428, 720-725 (2016). 
   
6. H. Müller, H.-P. Kley, Retrospective study on the reliability of an "approximate LD50" determined with a small number of animals. *Archives of Toxicology* 51, 189-196 (1982). 
   
7. T. A. Rasmussen et al., Panobinostat, a histone deacetylase inhibitor, for latent-virus reactivation in HIV-infected patients on suppressive antiretroviral therapy: a phase 1/2, single group, clinical trial. *Lancet HIV* 1, e13-21 (2014). 
   
8. S. Chia et al., Phenotype-driven precision oncology as a guide for clinical decisions one patient at a time. *Nat Commun* 8, 435 (2017). 
   
9. S. Corless, C. Naughton, N. Gilbert, Profiling DNA supercoiling domains in vivo. *Genom Data* 2, 264-267 (2014). 
   
10. C. J. Dorman, M. J. Dorman, DNA supercoiling is a fundamental regulatory principle in the control of bacterial gene expression. *Biophys Rev* 8, 209-220 (2016). 
   
11. H. A. Rahdar et al., Correlation between biofilm formation and carbapenem resistance among clinical isolates of. *Ethiopian Journal of Health Sciences* 29, 745-750 (2019). 
   
12. J. Larkins-Ford, B. Aldridge, Advances in the design of combination therapies for the treatment of tuberculosis. *Expert Opin Drug Dis* 18, 83-97 (2023). 
   
13. N. Principi, E. Silvestri, S. Esposito, Advantages and Limitations of Bacteriophages for the Treatment of Bacterial Infections. *Front Pharmacol* 10, 513 (2019). 
   
14. Y. Li et al., Bacteriophages allow selective depletion of gut bacteria to produce a targeted-bacterium-depleted mouse model. *Cell Reports Methods* 2, 100324 (2022). 
   
15. S. Uyttebroek et al., Safety and efficacy of phage therapy in difficult-to-treat infections: a systematic review. *Lancet Infect Dis* 22, e208-e220 (2022). 
   
16. X. Wan, H. Hendrix, M. Skurnik, R. Lavigne, Phage-based target discovery and its exploitation towards novel antibacterial molecules. *Curr Opin Biotechnol* 68, 1-7 (2021). 
   
17. K. N. Zhang et al., Bacteriophage protein PEIP is a potent Bacillus subtilis enolase inhibitor. *Cell Reports* 40, (2022). 
   
18. A. Bhambhani et al., Bacteriophage SP01 Gene Product 56 Inhibits Bacillus subtilis Cell Division by Interacting with FtsL and Disrupting Pbp2B and FtsW Recruitment. *Journal of Bacteriology* 203, (2021). 
   
19. B. Liu et al., Bacteriophage Twort protein Gp168 is a beta-clamp inhibitor by occupying the DNA sliding channel. *Nucleic Acids Research* 49, 11367-11378 (2021). 
   
20. R. Srinivasan et al., Bacterial Biofilm Inhibition: A Focused Review on Recent Therapeutic Strategies for Combating the Biofilm Mediated Infections. *Front Microbiol* 12, 676458 (2021). 
   
21. D. J. Wozniak, R. Keyser, Effects of subinhibitory concentrations of macrolide antibiotics on Pseudomonas aeruginosa. *Chest* 125, 62S-69S; quiz 69S (2004).

### 64. 
C. A. Mann et al., Novel bacterial topoisomerase inhibitors: unique targeting activities of amide enzyme-binding motifs for tricyclic analogs. Antimicrob Agents Chemother 67, e0048223 (2023).

```markdown
Figure 1: Belinostat is a cross-species HU inhibitor and a bacterial growth inhibitor. 

(A) The structural formula of Belinostat. 
(B) 1D NMR WaterLOGSY spectra of Belinostat (black) and Belinostat with SaHU (red). 
(C) The MST result of Belinostat-SaHU interaction. 
(D) EMSA showing that Belinostat inhibits SaHU-dsDNA interaction by replacing the dsDNA out of the SaHU. 
(E) AST (left) for Belinostat using S. aureus. The MICs (right) determined for S. aureus and 9 clinically isolated MRSA. 
(F) The Gram staining and TEM images of B. subtilis with or without Belinostat treatment, as well as overexpressing Gp46. Gram staining scale bar: 5 µm. TEM scale bar: 500 nm. 
(G) The Gram staining and TEM images of S. aureus with or without Belinostat treatment. The TEM images show the loss of nucleoid structure after the treatment. Gram staining scale bar: 5 µm. TEM scale bar: 200 nm.

| DMSO | 50 μg | 100 μg | 200 μg | 500 μg |
|------|-------|--------|--------|--------|
| 10^-8 | 900 | 905 | 910 | 915 | 920 | 925 |
| Belinostat (M) | Fnorm [‰] |
| KD = 4.24 ± 0.24 μM |
| ATCC29213 | CI 1 | CI 2 | CI 3 | CI 4 | CI 5 | CI 6 | CI 7 | CI 8 | CI 9 |
| 0 | 100 | 200 | 300 | 400 | 500 |
| MIC (μg/mL) |
| Belinostat | Belinostat (μM) | SaHU (20 nM) | dsDNA (1 nM) |
| 0 | 0 | 1 | 5 | 20 | 50 | 100 |
| - | + | + | + | + | + | + | + | + | + | + | + | + |
```

```markdown
Figure 2: CHADs are cinnamic hydroxamic acid derivatives.

(A) The commercially available anti-cancer drug: Belinostat and Panobinostat - with the shared HA and CHAD groups indicated by orange and blue square, respectively. 
(B) The HDAC inhibitor Vorinostat that contains only HA group. 
(C) Two HDAC inhibitors (phase 1 clinical trial passed) - Dacinostat and Pracinostat that contain HA and CHAD groups. 
(D) R4Cl and R24Cl representing adding R groups to CHA. 
(E) The structural formulas of R4F, R4Br and CHA. 
(F) The structural formula of cinnamic acid. * Maximum solubility reached.

|  | Belinostat | 400 μg/mL | Panobinostat | 150 μg/mL |
|  |------------- |------------|--------------|-----------|
| A| Vorinostat  | N/A        | Dacinostat   | >150 μg/mL* |
| B| Pracinostat | >150 μg/mL*| R4Cl         | 30 μg/mL    |
| C| R24Cl       | 30 μg/mL   | R4F          | >150 μg/mL* |
| D| R4Br        | >45 μg/mL* | Cinnamic hydroxamic acid | >200 μg/mL* |
| E| Cinnamic acid | N/A      |              |             |
```

```markdown
Figure 3: CHADs Target Site 1 of SaHU.

(A) The crystal structure of SaHU with D15 is colored in red. 
(B) The NMR backbone assignment of SaHUD15G mutant. 
(C) Overlay of 1H-15N HSQC spectra of SaHUD15G (black) and SaHUD15G with 5 molar equivalents of Panobinostat added (red). 
(D) After Panobinostat treatment (left), the exposed residues of SaHUD15G that experienced significant peak broadening effect as demonstrated in (C) and Fig. S7A are highlighted in pink on the structure. After R4Cl treatment (right), the exposed residues of SaHUD15G that experienced significant peak broadening effect as demonstrated in Fig. S7B and Fig. S7C are highlighted in orange. G46 (not assigned) and K41 (untraceable) are highlighted in blue. 
(E) Proposed SaHU-CHAD complex model (2:2). 
(F) H-bond network between R4Cl and G46, G48, A, B, C, E, G, K80, K83, dsDNA, α-helical region. 

![Figure](insert_image_link_here)
```

The text has been cleaned and formatted into markdown below:

```
K83 in the proposed model.  
(G) Proposed mechanism of competition between CHADs and DNA for HU binding.
```

```markdown
Figure 4: CHADs are effective against Gram-positive bacteria and some Gram-negative bacteria.

(A) The MICs of Panobinostat (upper) and R4Cl (lower) for 50 clinically isolated MRSA.
(B) The MICs of R4Cl for M. tuberculosis and an XDR-TB strain using Resazurin microtitre plate assay.
(C) The MIC determination of R4Cl for A. baumannii.

| MIC (µg/mL)     | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16  | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
|-----------------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|-----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Panobinostat   |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |     |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| R4Cl            |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |     |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |

H37Rv        XDR-TB
R4Cl (μg/mL)
Media              0    0.1   0.5   1     5    10   12   14   16
Control            1 µg/mL   2 µg/mL   4 µg/mL   6 µg/mL   8 µg/mL   10 µg/mL   12 µg/mL   14 µg/mL
0.0     0.5    1.0    1.5
OD600
A. baumannii
```

```markdown
# Figure 5: The effectiveness of CHADs in mice models

- (A) Histopathological assessment of heart, liver, kidney, lung, and spleen tissues in mice after injection of Belinostat (44 mg/kg), Panobinostat (28 mg/kg), R4Cl (44 mg/kg), or negative control buffer 7 days. Scale bar: 100 µm.
- (B) Bacterial counts (CFU/skin lesion) in S. aureus infected mice skins after treatment with negative control buffer, FA (2%), and Belinostat (0.001, 0.01, 0.1, and 1 µM), respectively.
- (C) Histopathological assessment of S. aureus infected mice skins after treatment with negative control buffer, FA (2%), and Belinostat (0.001, 0.01, 0.1, and 1 µM), respectively. Scale bar: 200 nm.
- (D) Bacterial counts (CFU/skin lesion) in FA-resistant MRSA infected mice skins after treatment with negative control.

![Figure](path-to-image)

## Experimental Setup
- Control: Negative control buffer
- Panobinostat
- R4Cl
- Belinostat
- FA (Fulvic acid)
- Vorinostat

## Dosages
- Belinostat: 40 mg/kg
- Panobinostat: 28 mg/kg
- R4Cl: 44 mg/kg
- FA: 2%
- Belinostat concentrations: 0.001, 0.01, 0.1, and 1 µM

## Timeline
- Inject with S. aureus
- Inject with Belinostat
- Record survival rate
- Inject with R4Cl
- Record survival rate
```

```markdown
- Histopathological assessment of FA-resistant MRSA infected mice skins after treatment with negative control buffer, FA (2%), Vorinostat, R4Cl, Panobinostat, and Belinostat, respectively. Scale bar: 200 nm.
- Kaplan-Meier survival curves (n=10) of the solvent used in this study (untreated) and Belinostat (40 mg/kg) injected S. aureus sepsis mice that monitored for 48 hours.
- Kaplan-Meier survival curves (n=10) of the solvent used in this study (untreated) and R4Cl (3 mg/kg) injected S. aureus sepsis mice that monitored for 48 hours.
```

# Figure 6: The anti-biofilm property of R4Cl

- (A) The Log2 (intensity) values of SaHU in different forms determined by MS.
- (B) Inhibition of P. aeruginosa biofilm formation by R4Cl. 
  - Upper panel: the crystal violet assay with the image shown above the chart as a representative. 
    - Negative Control (Control): 1% DMSO. 
  - Lower panel: the SEM images of the biofilm (Control) and those treated with R4Cl (Treated). 
    - Scale bar: 20 µm. 
- (C) Eradication of biofilms formed by S. aureus (ATCC 25923) and P. aeruginosa by R4Cl. 
  - Upper panel: the crystal violet assays with the images shown above the charts as representatives. 
    - Negative Control (Control): 1% DMSO. 
  - Lower panel: the SEM images of the biofilm (Control) and those treated with R4Cl (Treated). 
    - Scale bar: 20 µm. 

|          | Growth Medium | Cellular Material | Biofilm |
|----------|---------------|-------------------|---------|
| SA       | 25.5          | 26.0              | 26.5    |
| SA + R4Cl| 27.0          | 27.5              |         |

### (B) Biofilm Inhibition (%)
| Concerntration (!g/mL) | Biofilm Inhibition (%) |
|------------------------|------------------------|
| 0                      | 0                      |
| 20                     | 10                     |
| 40                     | 20                     |
| 60                     | 30                     |
| 80                     | 40                     |
| 100                    | 60                     |

### (C) Biofilm Eradication (%)
| Concerntration (!g/mL) | Biofilm Eradication (%) |
|------------------------|-------------------------|
| 0                      | 0                       |
| 20                     | 10                      |
| 40                     | 20                      |
| 60                     | 30                      |
| 80                     | 40                      |
| 100                    | 60                      |

Control versus Treated:

- P. aeruginosa
  - Control
  - Treated
- S. aureus

```markdown
Figure 7: The supercoiling relaxation and the antibiotic synergy effect of R4Cl.

(A) The representative bTMP staining images of E. coli and R4Cl-treated E. coli (right panels). The number represents the normalized fluorescence intensity of the current frame. Nucleoids were counterstained with DAPI and merged images were shown (left panels). Scale bar: 2 μm. The fluorescence intensity of E. coli and R4Cl-treated E. coli (lower).

(B) The representative bTMP staining images of B. subtilis and R4Cl-treated B. subtilis (right panels). The number represents the normalized fluorescence intensity of the current frame. Nucleoids were counterstained with DAPI and merged images were shown (left panels). Scale bar: 2 μm. The fluorescence intensity of B. subtilis and R4Cl-treated B. subtilis (lower). Statistics: two-tailed t test. Mean with SD. ns, not significant; **, p < 0.01; ****, p < 0.0001.

(C) The Gram staining images of E. coli, CB-treated E. coli, and E. coli treated with R4Cl.

|            |                             |                               |
|:----------:|:---------------------------:|:-----------------------------:|
|            | E. coli                     | E. coli + CB                  |
|            | E. coli + CB + R4Cl          | B. subtilis                   |
|            | B. subtilis + R4Cl           |                               |
|  1         | 10                          | 100                           |
|  1000      | 10000                       | 100000                        |
|            | Fluorescence Intensity (AU)  |                               |
|            | !!!!                        |                               |
|            | E. coli                     | E. coli + R4Cl                |
|  891       | 456                         |                               |
|            | B. subtilis                 | B. subtilis + R4Cl            |
|  8465      | 3841                        |                               |
|  2 μm      | 2 μm                        | 2 μm                          |
|  2 μm      | 2 μm                        | 10 μm                         |
|  10 μm     | 10 μm                       | 10 μm                         |
|            | E. coli CB-treated vs Non-treated |                           |
|            | E. coli CB + R4Cl-treated vs CB-treated |                    |
|  0.00      | 0.05                        | 0.10                          |
|  0.15      | 0.20                        |                               |

Pathways:
- Purine metabolism
- Exopolysaccharide biosynthesis
- Two-component system
- ABC transporters
- Methane metabolism
- Fructose and mannose metabolism
- Alanine, aspartate and glutamate metabolism
- Amino sugar and nucleotide sugar metabolism
- One carbon pool by folate
- Biofilm formation - Escherichia coli
- Sulfur metabolism
- beta-Lactam resistance
- RNA degradation
- Cationic antimicrobial peptide (CAMP) resistance
- Biosynthesis of nucleotide sugars
- O-Antigen nucleotide sugar biosynthesis
- Phosphotransferase system (PTS)
- Ribosome
- Glyoxylate and dicarboxylate metabolism
- Pantothenate and CoA biosynthesis

| Pathway                                      | GeneRatio  | count | padj |
|----------------------------------------------|------------|-------|------|
| Ribosome                                     | 5.00       | 14.83 | 0.0  |
| Microbial metabolism in diverse environments | 0.2        | 0.4   | 0.1  |
| Oxidative phosphorylation                    | 0.6        | 0.8   | 0.2  |
| Carbon metabolism                            | 0.3        |       |      |
| Selenocompound metabolism                    | Ribosome   |       |      |
| Glyoxylate and dicarboxylate metabolism      | Sulfur metabolism |            |      |
| Glycolysis / Gluconeogenesis                 | Citrate cycle (TCA cycle) |   |      |
| Pentose phosphate pathway                    | Lipoic acid metabolism     |   |      |
| beta-Lactam resistance                       | Lysine degradation         |   |      |
| Methane metabolism                           | Nitrogen metabolism        |   |      |
| Pyruvate metabolism                          | Glycine, serine, and threonine metabolism | |      |
| Biosynthesis of secondary metabolites        | Arginine and proline metabolism           | |      |
| Nucleotide excision repair                   |----------------------------------------------|--------|------|

```

```markdown
simultaneously with CB and R4Cl. Scale bar: 20 µm. 

(D) KEGG pathway enrichment analysis of differentially expressed genes between 10 µg/mL of CB treated and untreated E. coli cells. Y-axis indicates the pathway name; x-axis indicates gene ratio. The bubble size indicates the number of genes and the color bar indicates the adjusted p-value. 

(E) KEGG pathway enrichment analysis of differentially expressed genes between 10 µg/mL of CB and 10 µg/mL of R4Cl simultaneously treated and only 10 µg/mL of CB treated E. coli cells. Y-axis indicates the pathway name; x-axis indicates gene ratio. The bubble size indicates the number of genes and the color bar indicates the adjusted p-value. 

(F) The synergy of R4Cl with rifamycin for M. tuberculosis with a calculated FIC. 
```

## Material and methods

### Virtual screens

OpenMM (1) was used for energy minimization of the 2.14 Å SaHU structure (PDB code 4QJN). The coordinate of Ca of K80 of site 1 was set as the center of the docking grid box with a size of 20Å3, and for site 2, the coordinate of I71 Ca was used. AutoDock Vina (v1.2.0) (2) was used to dock the molecules of both DrugBank (3) and ZINC20 (4) to SaHU. Additionally, CPI scores were also predicted using Pangu Drug Model CPI predictor (5) for the molecules from DrugBank. The geometric means of the docking and CPI scores were used to rank the molecules as previously described (6).

All DrugBank molecules are ranked based on their combined scores and listed in Supplementary Table 1 and 2. The top 1000 compounds for ZINC20 are ranked by docking score and listed in Supplementary Table 3 and 4.

### Cloning, expression and purification of the recombinant HU proteins

All HU genes were chemically synthesized and amplified by PCR. The PCR products were purified by 1.5% agarose gel electrophoresis and ligated into respective linearized expression vector based on Gibson-assembly. The cloned plasmids were transformed into E. coli strain DH5α and verified by sequencing. Site-directed mutagenesis was performed using the Q5 Site Directed Mutagenesis Kit (NEB, Cat#E0552S). All primers and plasmids are shown in Supplementary Table 6.

The vectors were then transformed into BL21(DE3) cells to express recombinant proteins. Bacterial cultures were incubated at 37°C in LB medium or M9 medium (for isotopic labeling, using 15N-labelled NH4Cl and/or 13C-labelled glucose) containing relevant antibiotics, grown to.

### Protein Purification

OD600 of ~ 0.6 and induced by 1 mM IPTG. After shaking at 18°C for 16-18 hours, the cells were harvested by centrifugation at 5,000 rpm for 10 min at 4°C and resuspended in a 30 mL binding buffer (50 mM NaH2PO4, 300 mM NaCl, 10 mM imidazole and pH 8.0). The cells were then lysed by sonication and centrifuged at 20,000 rpm at 4°C for 30 min. The supernatants of cell lysate were loaded onto the Ni-NTA agarose resin (Qiagen, Cat#30250) in the presence of binding buffer. The resin was washed by a wash buffer (binding buffer with 20 mM imidazole) and then the recombinant proteins were eluted by an elution buffer (binding buffer with 250 mM imidazole). The eluted fractions were dialyzed against the storage buffer (50 mM NaCl, 20 mM Tris, pH 7.4). As for SUMO-HU, the elution was also digested with protease Ulp1. The SUMO tag and Ulp1 were removed by the second immobilized metal affinity chromatography. And the HUs were loaded on a 5 mL HiTrap Heparin HP column (GE Healthcare Life Sciences), eluting with a linear gradient of 0.05-1.5 M NaCl. The recombinant proteins were further purified by size exclusion chromatography using a Superdex 200 Hiload 16/600 column (GE Healthcare Life Sciences), which were equilibrated with the storage buffer, on an ÄKTA pure system (GE Healthcare Life Sciences). The concentrations of the proteins were estimated by the Bradford protein assay.

### WaterLOGSY Experiments

The 1D NMR WaterLOGSY experiments of 500 µM compounds were carried out at 298 K using an 800 MHz Avance Neo spectrometer (Bruker) equipped with a cryogenic probe, followed by WaterLOGSY experiments of samples consisting of 10 µM HUs and 400 µM compounds. All samples were prepared in the storage buffer, containing 5% DMSO and 10% D2O.

## WaterLOGSY Pulse Sequence

WaterLOGSY (ephogsygpno) pulse sequence from Bruker was used for data acquisition with 256 scans.

## Binding Affinity Determination by MST

Due to the strong non-specific binding of CHADs to the probes or chips, biolayer interferometry (BLI) or surface plasmon resonance (SPR) did not produce reproducible results for the CHADs-SaHU interactions. An equilibrium could not be established in isothermal titration calorimetry (ITC) due to the poor solubility of the CHADs. MST was used for the binding affinity determination. 

MST was performed to study the interactions between SaHU and the inhibitors. Purified SaHU was labelled with a fluorescent dye using the Protein Labelling Kit RED-NHS kit (NanoTemper Technologies, CAT#MO-L011) according to the manufacturer’s instructions. 

Binding assays were performed with a Monolith NT.115 device (NanoTemper Technologies) using standard treated capillaries. Compounds were serially diluted two-fold in MST buffer (PBS containing 500 mM NaCl and 0.05% Tween-20, pH 7.4). The concentration of labelled protein was kept to a minimum (20 nM). Equal amounts of labelled protein were titrated with varied ligand concentration (0.24 µM to 0.5 mM). The dissociation constant (KD) values were obtained by fitting the binding curve with the NT Analysis software from Nano Temper Technologies.

## EMSA

The sequences of the oligonucleotides used in EMSA are listed in Supplementary Table 6. The 5’ end of the leading strand was labelled with FAM. The 21 bp dsDNA was prepared by annealing the labelled leading strand to its non-labelled complementary oligonucleotide.

Belinostat was dissolved in DMSO to prepare a stock solution with a concentration of 100 mM. SaHU and the 21 bp dsDNA were pre-incubated on ice for 30 min. Different concentrations of Belinostat were added to the SaHU-dsDNA complex, respectively. After adding Belinostat, the mixtures were incubated on ice for 5 min and then loaded onto a 7% (w/v) non-denaturing polyacrylamide gel. The electrophoresis was performed at 90 V in 0.5 × TBE buffer on ice. The image was captured by a ChemiDocTM MP Imaging System (Bio-Rad).

### AST and MIC determination

The AST using disk diffusion method were performed prior to the MIC determination according to CLSI standards. Briefly, each compound was dissolved in DMSO at a moderate. 20 µL of each drug solution was added to a blank disk before use. Disks containing DMSO were used as negative controls. A direct LB broth suspension of S. aureus was prepared by isolating colonies from an 18- to 24-hour LB agar plate and then adjusted to a turbidity equivalent to a 0.5 McFarland standard using a photometric device. Within 15 min after adjusting the turbidity of the inoculum suspension, a sterile cotton swab was dipped into the suspension and then streaked over the entire sterile LB agar surface to ensure even distribution of the inoculum. The lids were ajar for 3-5 min to allow any excess surface moisture to be absorbed before applying the drug-impregnated disks. The plates were incubated at 37°C for 24 hours. The images were captured by a ChemiDocTM MP Imaging System (Bio-Rad).

For the MIC determination, 100 µL of the mixtures containing bacterial suspensions and the small molecules to the required final concentration in 96-well flat-bottom plates. The final cell density of each well was approximately 5 × 105 CFU/mL. Plates were then incubated at 37°C.

Without shaking overnight until untreated control cultures reached stationary phase. Then plates were read at 600 nm using a Cytation 5 plate reader (BioTeK). All MICs expect for M. tuberculosis were determined at the BioBank, the first affiliated hospital of Xi’an Jiaotong University (Biosafety level 2). The MICs for M. tuberculosis and the XDR-TB strain were detected by resazurin microtitre plate assay in Henan Center for Disease Control and Prevention (Biosafety level 3). Bacterial suspension equivalent in turbidity to that of 1 McFarland standard was diluted 1:200 in Middlebrook 7H9 broth. 200 µL inoculum and various concentrations of R4Cl were added in each well of a 96-well plate. Plates were sealed and incubated at 37°C for 2 weeks. Resazurin solution (0.02%) was added to the plates (25 µL/well) and incubated at 37°C for 24 hours. The MIC was determined as the corresponding solution showing blue color. All experiments containing at least three technical replicates were repeated at least twice. All bacterial strains used are listed Supplementary Table 7. Quality control was performed for each bacterium using tobramycin for Gram-positive bacteria (except for M. tuberculosis), erythromycin for Gram-negative bacteria, and rifamycin for M. tuberculosis (Fig. S13B). 

### Gram staining and TEM
B. subtilis (strain 168), S. aureus, and E. coli were grown at 37°C overnight in 3 mL of LB medium and diluted 1:100 (v/v) into fresh LB medium. B. subtilis (strain 168) and S. aureus were treated with or without 400 µg/mL (1.26 mM) of Belinostat for another four hours, while E. coli was exposed to 10 µg/mL of CB, 10 µg/mL of R4Cl, or 10 µg/mL of CB and 10 µg/mL of R4Cl. The Gp46-overexpressed B. subtilis strain was prepared as described previously.

For Gram staining, bacteria were harvested by centrifugation at 4,000 rpm for 10 min and washed twice with PBS buffer. The cells were resuspended in PBS and 5 µL of the bacterial

The suspension was spread onto clean glass slides to create thin films. The slides were passed through a flame 3-4 times to heat-fix the bacteria to the slide. For Gram staining, the slides were strained firstly with crystal violet solution for 1 min followed by Gram’s iodine solution for another 1 min. 95% ethanol was used to decolorize the slides, and the safranin solution was used as a counterstain. The slides were air-dried and covered with cover slips. Images were taken with a CX23 upright microscope (Olympus).

For the TEM, the samples were prepared as described (9). The prepared sample sections were examined with a JEM-1400 FLASH Transmission Electron Microscope (JEOL). Three technical replicates were performed to ensure the consistency of the observation.

Lead compound library expansion
The compound expansion was performed online using PGMO, part of Pangu Drug Model (5). 1820 molecules were generated and ranked by the Quantitative Estimate of Druglikeness (QED) were listed in Supplementary Table 5.

X-ray crystallography
The SaHU protein was diluted to 8 mg/mL for crystallization. Crystals grew with hanging drops at 16°C in crystallization buffer (0.1 M MES pH 6.0, 15% w/v PEG 3,350, 20% glycerol). The crystals were mounted and flash-frozen in liquid nitrogen. Diffraction data were collected at the Shanghai Synchrotron Radiation Facility beamline BL02U1, and a total of 360 frames were recorded with 1-degree oscillation. For structure determination and analysis, HKL2000 was used to index, integrate, and scale the data (10). Molecular replacement was performed with PHASER.

## Title: Protein Structure Determination and Analysis

- **Structure Determination**
  - The structure of the protein was determined using the search model of SHU (PDB ID: 4QJN). The final model was built with COOT (11) and refined in PHENIX (12). The model quality was analyzed by Molprobity (13) and deposited in the Protein Data Bank with accession code 8HD5. Statistics from data collection, processing and structure refinement are summarized in Supplementary Table 8. 

- **NMR Backbone Assignment and Titration Experiment**
  - The triple resonance experiments were performed in a buffer containing 500 mM NaCl, 50 mM KH2PO4, 10% D2O, and pH 7.4. NMR spectra were collected at 298 K using an 800 MHz Avance Neo spectrometer (Bruker) equipped with a cryogenic probe. Spectral assignments were completed using our in-house, semi-automated assignment algorithms and standard triple-resonance assignment methodology. 

- **NMR Titration Experiment**
  - The NMR titration experiments were performed in the storage buffer containing 5% DMSO and 10% D2O. 1H-15N HSQC spectra were acquired at 298 K for each sample, and the intensity change (I/I0) was calculated, where I and I0 correspond to the peak intensity of the bound and free SaHUD15G, respectively. 

- **HADDOCK Model**
  - The exposed residues of SaHU (as shown in Fig. 3D) that experienced major peak broadening effects, i.e., L29, D40, T43, L44, I45, E51, K80, A81, and K83 were chosen as the active residues, and the surrounding residues were designated as passive residues. All atoms of R4Cl were used to build a model of a 2:2 complex with one R4Cl bound to one subunit of SaHUD15G.

# HADDOCK (v2.2)

An ambiguous distance restraint of 2.0 Å was invoked between all active and passive residues of the other protein partner. The interfacial residues were allowed to move during the simulated annealing and water refinement. A total of 1,000 initial complex structures were generated by rigid-body energy minimization, and the best 200 by total energy was selected for torsion angle dynamics and subsequent Cartesian dynamics in an explicit water solvent. The best structure was chosen based on interactional energy.

## MD simulation

The MD simulation of the CHAD-SaHUD15G complex was conducted using Molecular Mechanics Poisson-Boltzmann Surface Area (MMPBSA) to evaluate the protein-ligand interaction. The MMPBSA simulation was implemented through the SPONGE package, which provided the protein-ligand binding free energy and estimation of the energy contribution per residue to the binding. The topology of the protein was constructed using the ff99sb force field, and the ligand topologies were generated from the gaff force field with bcc charges. The water model (tip3p) was used to solvate the system in a dodecahedron unit cell. The fully solvated system was then neutralized with a sodium ion. A 2 ns production phase MD simulation was generated using SPONGE. The free energy calculation was based on the PBSA model, and the energy decomposition to each residue was performed by AmberTools22.

## RBFE calculation

The RBFE calculations were performed using our in-house SPOGNE-FEP based on SPONGE, a GPU-accelerated molecular dynamics package that utilizes enhanced sampling and AI-driven algorithms.

## Algorithms and RBFE Calculation

Algorithms were utilized to improve accuracy (16). Belinostat was used as the reference compound, and the R4Cl-SaHU model was employed as the complex structure in the RBFE calculation for all MIC-determined molecules listed in Fig. 2. The calculations were performed on a Nvidia V100 GPU computer and took approximately 4 hours for one pair of molecules.

## MBC Determination

The cidality assay was carried out following the CLSI M26-A guideline. An exponential culture of S. aureus was diluted to 5 ~ 7.5 × 10^5 CFU/mL in 2 mL of LB medium, supplemented with 0 (growth control), 2, 4, 6, 8, 16, and 32 times the MIC of R4Cl. The samples were incubated at 37°C without shaking. The final inoculum was confirmed by actual count. Tubes were vortexed and re-incubated at 20 hours, then vortexed and re-incubated again before sampling at 24 hours. Aliquots of the culture (0.1 mL) were diluted once in antibiotic-free LB. Both 0.1 mL of the culture and 0.1 mL of the dilution were streaked onto agar plates separately. The plates were incubated at 37°C for 24 hours, and the colonies were counted. The lethal endpoint was defined as 99.9% killing (≥ 3 log10 drop in CFU/mL) of the final inoculum. The MBC for R4Cl against S. aureus was found to be at 16 times the MIC, suggesting that R4Cl is bacteriostatic.

## FoR

Log-phase S. aureus at concentrations ranging from 10^6 to 10^10 CFU/mL were plated onto LB agar plates containing R4Cl at eight times its MIC. The plates were incubated at 37°C for 48 hours. Additionally, dilutions of each culture were plated on drug-free LB agar to ensure accurate colony counts. Resistance frequencies were calculated by dividing the number of 

---
Cleaned and formatted by [Assistant Name]

## Resistant colonies calculation

The frequency of resistant colonies was calculated by dividing the number of resistant colonies by the total number of CFU plated. Each experiment was performed in triplicate, and the reported frequency represents the average value.

## Genome sequence analysis

Sourmash was used to compute sourmash signature for every bacteria assembled genome and produce the similarity heatmap as previously described (19). The collection of the clinical isolates was approved by the Committee of Ethics (Approval NO. 2022-1120).

## Toxicity Assay of CHADs in Mice

All experimental procedures were conducted in accordance with animal welfare guidelines and were previously approved by the Animal Welfare and Ethics Committee of Xi'an Jiaotong University, Xi’an, China (Approval No. 2021-1513). In these studies, 6- to 7-week-old female specific pathogen-free (SPF) Kunming mice purchased from the Laboratory Animal Center of Xi'an Jiaotong University (Xi’an, China) were used. Animals were housed under standard conditions of humidity (50 ± 10%), temperature (22 ± 2°C), and light-dark cycle (12 hours each) with free access to food and water.

To assess the percutaneous toxicity of CHADs in mice, the mice were orally administered 45 μL of Ibuprofen suspension 1 hour before being anesthetized with isoflurane. An exposed skin area (2 cm × 1 cm) was created by depilating the back skin of the mice using hair removal cream. Kunming mice were randomly divided into four groups (n = 6) and weighed once a day. Considering the low solubility, CHADs were dissolved in 10% DMSO and 90% PEG 400. A dose of 1000 mg/kg of Belinostat, Panobinostat, or R4Cl was applied to medical gauze.

Medical gauze was placed snugly against the exposed skin of the mice and secured with medical tape to ensure it did not interfere with the normal activities of the mice. The gauze was removed after 4 hours. The exposed skin of the mice was gently wiped with a cotton ball dampened with warm water. These steps were repeated for seven consecutive days, and the health conditions of the mice were observed daily. The mice were euthanized and dissected seven days later, and the heart, liver, spleen, lung, and kidneys were collected for further analysis.

Belinostat, Panobinostat, and R4Cl were formulated in 10% DMSO, 40% PEG 400, 5% Tween-80, and 45% saline. For the acute toxicity assay, the LD50 of a single compound was determined via intravenous injection using the up-and-down procedure (20). The estimated initial LD50 was 175 mg/kg. Sigma was 0.2, the slope was 5, and T was 1.6. The sequential dosages were calculated using AOT425-StatPgm. The first dosage of 175 mg/kg was administered to the first mouse. If it survived within 24 hours, 280 mg/kg was given as the second dose according to the sequential dosages. If it died, the mouse was dissected, and 110 mg/kg was chosen. Tests continued until the standard stopping criteria were met. All surviving mice were monitored for signs of toxicity and then euthanized and dissected 14 days later. For the multiple-dose assay, CHADs were administered daily via intravenous injection for seven consecutive days. Belinostat and R4Cl were given at a daily dose of 44 mg/kg, and Panobinostat was given at 28 mg/kg (n = 6 for each compound). Control mice received the same volume of the solvent. The mice were monitored for signs of toxicity, weighed daily, and then euthanized and dissected 7 days later.

Mice were anesthetized with isoflurane, and whole blood was collected from the retro-orbital venous plexus using a 1 mg/mL EDTA solution as an anticoagulant. After blood collection, the

## Samples Preparation

Samples were gently inverted several times to mix well and then stored at 4°C. Blood cells and platelets were analyzed using a blood analyzer (Kangte). After decapitation, the tissues were promptly fixed in 4% paraformaldehyde for 24 hours. The organs were then washed and dehydrated through a series of graded ethanol baths before being embedded in paraffin wax. Serial sections, each 5 µm thick, were cut using a microtome, stained with H&E, and examined using a NanoZoomer S60 (HAMAMATSU).

## Mouse Superficial Skin Infection and Sepsis Model

The animal tests were adapted from a previously described skin infection model in mice (21) and performed at BioBank, the first affiliated hospital of Xi’an Jiaotong University, with approval from the Committee of Animal Ethics (Approval NO. 2021-1513). The 6- to 7-week-old female specific pathogen-free (SPF) BALB/c mice were used for the experiments, with n = 6 for every group. 

First, the mice were orally administered 45 μL of Ibuprofen suspension 1 hour before being anesthetized with isofluorane. An exposed skin area (2 cm × 1 cm) was created by depilating the back skin of the mice using hair removal cream. Afterward, medical tape was used by the same operator to attach to the depilated skin, and it was avulsed 20 times after applying the same pressure by pressing with their fingers. The medical tape was replaced in each paste-avulsion process for better removal of the stratum corneum. 

S. aureus and FA-resistant MRSA with ~ 107 CFU/mL, were immediately applied to the skin of each animal using 20 μL bacterial suspension. After inoculation for 24 hours, a group of mice were euthanized and the 2 cm² infected wound skin was promptly removed through surgery to quantify the infectious dose before any treatment was given. The skin was immediately serially diluted in saline, crushed, and ground using a tissue homogenizer. The suspensions were diluted with saline and the dilutions.

```markdown
- For the skin wound infection model, 8-week-old female BALB/c mice were used, with n = 10 for each group. The mice were infected with 5 × 109 CFU of MRSA by applying a suspension of bacteria to a 2 cm² area of the skin on the back after the hair was removed and the skin was scratched with a sterile needle. After 30 min of evaporation of the bacteria, the remaining mice were divided into various groups and treated on day 1. Treatment was started 4 hours post-infection and continued daily for 3 consecutive days. On the day of infection, 100 μL of 90% saline containing 10% PEG 400 was applied to the skin lesions. The small molecules Belinostat and R4Cl, solubilized in 90% saline containing 10% PEG 400, were applied to the skin lesions at the desired concentration. The bacterial content per gram of tissue (CFU/g) was determined by homogenizing the skin tissue in saline, serially diluting the suspension, and plating a 10-fold dilution on LB agar plates. The plates were incubated at 37°C for 24 hours, and the colonies were counted and converted to CFU/g. Observations on food intake, drinking water, and mental status were made at least twice a day. There were no signs of systemic infection, weight loss, or distress in the mice throughout the study. On day 4, the mice were euthanized 12 hours after the last treatment. The infected skin area was excised, with half processed for histological examination using H&E staining and the other half for determination of bacterial content per gram of tissue (CFU/g) as described before.
  
- For the sepsis model, 8-week-old female BALB/c mice were utilized, with n = 10 for each group. The mice were administered lethal doses of S. aureus (1 × 108 CFU) or P. aeruginosa (8 × 108 CFU) via tail vein injection to induce septic shock. Belinostat and R4Cl were prepared in a solution consisting of 10% DMSO, 40% PEG 400, 5% Tween-80, and 45% saline. The solvent (control), 40 mg/kg of Belinostat or 3 mg/kg of R4Cl was administered intravenously after 5 hours. The mice were monitored for 48 hours post-drug injection and then sacrificed on day 3. Statistical analysis of Kaplan-Meier survival curves for each group of mice was conducted using the log-rank (Mantel-Cox) test.
```

# MS analysis of HU population in different forms

S. aureus was initially cultured in BHI broth at 37°C for 18 hours. 300 μL of the suspensions were diluted 1:100 (v/v) with BHI broth containing 1% glucose in 50 mL conical sterile polypropylene centrifuge tubes. 15 μg/mL (0.5 × MIC, 76 μM) of R4Cl was added and DMSO-treated S. aureus was used as a control. The samples were incubated statically at 37°C for 24 hours. Then the cultures were vortexed, and the microbial counts were detected by plate count.

The extraction of EPS was performed according to Akio Chiba et al. (24). Briefly, these cultures were centrifuged at 8,000 g for 10 min, and the supernatants (growth medium) were concentrated to 500 μL using 10 kDa ultrafiltration tubes. The sediments were resuspended with 500 μL of 1.5 M NaCl solution and centrifuged at 8,000 g for 10 min again. The supernatants contained biofilms. The bacteria were resuspended with 500 μL of PBS with 8M Urea added, lysed by sonication, and centrifuged at 20,000 rpm at 4°C for 10 min. The supernatants contained cellular material.

5 μL of 5 × loading buffer was added to 20 μL of each supernatant. 10 μL of each sample was loaded into each lane of 20% polyacrylamide gels in the Mini Trans-Blot Cell system (Bio-Rad) running at 210 V for 1 hour. Gels were stained with Coomassie brilliant blue for no less than 10 min followed by destaining in water overnight. The images were captured by a ChemiDocTM MP Imaging System (Bio-Rad). Sample lanes recycled from the SDS gel were digested with trypsin and desalted by C18 ZipTips (Millipore, Cat# ZTC18S096). The samples were analyzed by a Q-Exactive plus mass spectrometer (Thermo Fisher Scientific) coupled with an UltiMate 3000 RSLCnano system. Database search was performed by MaxQuant (25), and results are shown in Supplementary Table 9.

## Biofilm Formation Inhibition and Eradication Assays

Crystal violet assay was utilized for both the biofilm formation inhibition and eradication assays. The bacteria were initially cultured in BHI broth at 37°C for 18 hours. The suspensions were then adjusted to 0.5 McFarland standard. Subsequently, the suspensions were diluted 1:100 (v/v) with BHI broth containing 1% glucose to obtain suspensions containing 1 × 10^6 CFU/mL bacteria.

For the biofilm formation inhibition assay, standardized *P. aeruginosa* suspension at 10^6 CFU/mL was dispensed into each well of a 96-well plate. Various concentrations of R4Cl (0.625, 1.25, 2.5, 5, 10, and 20 μg/mL) were added to the bacterial suspension for the dose-dependent anti-biofilm assay. DMSO replaced the compound as a control, and uninoculated broth served as the blank. The plate was then incubated at 37°C for 24 hours under static conditions. After incubation, the wells were washed with PBS buffer, heat-fixed, and stained with filtered 0.5% crystal violet for 5 min at room temperature. Excess stain was removed by rinsing with water, and crystal violet-bound cells were solubilized with 33% acetic acid. The released stain was measured at 570 nm using a Cytation 5 plate reader (BioTeK). Each assay was conducted with three technical replicates and repeated three times. The figure presented shows one representative experiment.

For the eradication assay, *P. aeruginosa* and *S. aureus* were initially cultured in BHI broth at 37°C for 18 hours. Standardized suspensions containing 10^6 CFU/mL bacteria were incubated in...

### Experimental Procedure

96-well microtiter plates were incubated at 37°C for 24 hours to allow biofilm formation. Following incubation, the medium was removed, wells were rinsed with PBS, and various concentrations of R4Cl (10, 20, 30, 40, 50, and 60 μg/mL) were added and incubated for an additional 24 hours. The wells were then emptied, heat-fixed, stained with 0.5% crystal violet, rinsed, air-dried, and 33% acetic acid was added for absorbance measurement at 570 nm. DMSO was used as the negative control. Each assay was conducted with three technical replicates and repeated three times. The figure presented represents one representative experiment.

The biofilm inhibition rate or eradication rate was calculated using the following formula:

Biofilm inhibition/eradication (%) = (OD 570 negative control - OD 570 sample) / OD 570 negative control × 100%

### Biofilm Observation

Biofilm conditions were observed using scanning electron microscopy (SEM). For the biofilm formation inhibition assay, sterile polystyrene cover slips (1 mm thick and 5 mm in diameter) were placed into the wells of 6-well plates for biofilm formation. 2 mL of standardized P. aeruginosa suspension at 10^6 CFU/mL was dispensed into each well. 20 μg/mL of R4Cl was added. Polystyrene cover slips with cells grown in R4Cl-free medium were used as controls. The cover slips were then incubated at 37°C for 24 hours, washed three times with PBS to remove non-adherent bacteria, fixed, dehydrated, and prepared for SEM imaging.

For the eradication assay, sterile polystyrene cover slips were utilized and processed as described above. The samples were examined using an XL-30 ESEM (Philips) after critical-point drying and 1200 bar pressure at 40°C.

**Wells of 6-well plates**
2 mL of standardized P. aeruginosa and S. aureus at 10^6 CFU/mL was dispensed into each well and incubated at 37°C for 24 hours to form biofilms. Then, the medium was removed, wells were rinsed with PBS, and 60 μg/mL of R4Cl was added and incubated for another 24 hours. The remaining steps for the preparation of SEM samples are the same as those mentioned before.

**bTMP Incorporation and Imaging**
B. subtilis (strain 168) and E. coli were grown at 37°C overnight in 3 mL of LB medium and diluted 1:100 (v/v) into fresh LB medium. Bacteria were treated with or without 10 µg/mL of R4Cl for another four hours.

Bacterial cells were washed with PBS before they were permeabilized with 250 μg/mL lysozyme for 30 min at room temperature (RT). Cells were incubated with 0.5 mg/mL EZ-Link Psoralen-PEG3-Biotin (ThermoFisher Scientific) for 20 min, then exposed to 4 kJ m^-2 of 365 nm light using a UV Crosslinker (SGLinker UV Crosslinker) for 20 min on ice followed by a PBS wash. Cells were then fixed with 4% paraformaldehyde and treated with 0.2% Triton X-100 before they were incubated with Alexa Fluor 594 Streptavidin (ThermoFisher Scientific) for one hour at RT in the dark, washed with PBS, and stained with DAPI for 10 min. Cells were then mounted onto glass slides with ProLong Gold antifade mountant (ThermoFisher Scientific). Images were taken with Olympus FV3000 confocal microscope (Olympus). Fluorescence intensity was quantified using ImageJ software from multiple random fields obtained with identical acquisition settings and normalized by cell number.

# Transcription profiling

For RNA-Seq, *E. coli* was first grown overnight in LB medium and then an overnight culture was diluted 1:100 in fresh regular LB medium, LB with 10 μg/mL of CB, LB with 10 μg/mL of R4Cl, or LB with 10 μg/mL of CB and 10 μg/mL of R4Cl. Cells were incubated at 37°C for another four hours. Three biological replicates per sample were collected for each condition. Total RNA was isolated from each sample using RNeasy® Mini Kit (QIAGEN, Cat#74104), and ribosomal RNA was removed with Ribo-Zero Plus rRNA Depletion Kit (Illumina, Cat#20040529). The remaining RNA was fragmented, converted to cDNA (with dUTP incorporation for strand specificity), and used to create a sequencing library. Library quality was assessed with qBit, Agilent Bioanalyzer, and qPCR. Sequencing was performed on a PE 150 system (Illumina). Reads were mapped to the *E. coli* MG1655 reference genome using Bowtie2, and gene expression was quantified using FeatureCounts (normalized to RPKM). Differential gene expression was determined with DESeq2 (fold change > 1, adjusted p < 0.05). KEGG pathway enrichment analysis was performed using clusterProfiler. The RNA-seq data are available in the SRA under accession number: PRJNA1227296. 

# Growth curve

The bacterial growth assays were performed at 37°C in 96-well plates. The absorbance at 600 nm was measured at certain times using a Neo 2 multi-well plate reader (BioTek). At least three biological and technical replicates were performed for each growth curve test.

# In vitro synergy between R4Cl and Rifamycin

# Title: Study on in vitro synergy between R4Cl and Rifamycin

The checkerboard method, based on Resazurin microtitre plate assay as described above, was used to study in vitro synergy between R4Cl and Rifamycin. Rifamycin was added at concentrations between 0 and 0.5 μg/mL, and R4Cl was added at concentrations ranging from 0 to 12 μg/mL, as demonstrated in Fig. 7F. The Fractional Inhibitory Concentration Index (FIC) was determined using the formula: 

\[ \text{FIC} = \left( \frac{\text{MIC of Rifamycin in combination}}{\text{MIC of Rifamycin alone}} \right) + \left( \frac{\text{MIC of R4Cl in combination}}{\text{MIC of R4Cl alone}} \right) \]

Synergy was defined as an FIC < 0.5, indifference as an FIC between 0.5 and 4, and antagonism as an FIC > 4 (26).  

## References

1. P. Eastman et al., OpenMM 7: Rapid development of high performance algorithms for molecular dynamics. *PLOS Computational Biology* 13, e1005659 (2017). 

2. J. Eberhardt, D. Santos-Martins, A. F. Tillack, S. Forli, AutoDock Vina 1.2.0: New Docking Methods, Expanded Force Field, and Python Bindings. *Journal of Chemical Information and Modeling* 61, 3891-3898 (2021). 

3. C. Knox et al., DrugBank 6.0: the DrugBank Knowledgebase for 2024. *Nucleic Acids Research* 52, D1265-D1275 (2023). 

4. J. J. Irwin et al., ZINC20-A Free Ultralarge-Scale Chemical Database for Ligand Discovery. *Journal of Chemical Information and Modeling* 60, 6065-6073 (2020). 

5. X. Lin et al., PanGu Drug Model: learn a molecule like a human. *Science China-Life Sciences* 66, 879-882 (2023). 

6. R. Breitling, P. Armengaud, A. Amtmann, P. Herzyk, Rank products: a simple, yet powerful, new method to detect differentially regulated genes in replicated microarray experiments. *Febs Letters* 573, 83-92 (2004). 

7. R. M. Humphries et al., CLSI Methods Development and Standardization Working Group Best Practices for Evaluation of Antimicrobial Susceptibility Tests. *J Clin Microbiol* 56, (2018). 

8. P. Zhang et al., Bacteriophage protein Gp46 is a cross-species inhibitor of nucleoid-associated HU proteins. *Proc Natl Acad Sci U S A* 119, (2022). 

9. K. N. Zhang et al., Bacteriophage protein PEIP is a potent Bacillus subtilis enolase inhibitor. *Cell Reports* 40, (2022). 

10. Z. Otwinowski, W. Minor, in Methods in enzymology. (Elsevier, 1997), vol. 276, pp. 307-326. 

11. P. Emsley, B. Lohkamp, W. G. Scott, K. Cowtan, Features and development of Coot. *Acta Crystallographica Section D: Biological Crystallography* 66, 486-501 (2010). 

12. P. V. Afonine et al., Towards automated crystallographic structure refinement with phenix. refine. *Acta Crystallographica Section D: Biological Crystallography* 68, 352-367 (2012).

### References

1. V. B. Chen et al., "MolProbity: all-atom structure validation for macromolecular crystallography." *Acta Crystallographica Section D: Biological Crystallography*, 66, 12-21 (2010).
   
2. G. C. P. van Zundert et al., "The HADDOCK2.2 Web Server: User-Friendly Integrative Modeling of Biomolecular Complexes." *J Mol Biol*, 428, 720-725 (2016).
   
3. C. Wang et al., "Calculating protein-ligand binding affinities with MMPBSA: Method and error analysis." *J Comput Chem*, 37, 2436-2446 (2016).
   
4. Y. P. Huang et al., "SPONGE: A GPU-Accelerated Molecular Dynamics Package with Enhanced Sampling and AI-Driven Algorithms." *Chinese Journal of Chemistry*, 40, 160-168 (2022).
   
5. B. R. Miller et al., "MMPBSA.py: An Efficient Program for End-State Free Energy Calculations." *Journal of Chemical Theory and Computation*, 8, 3314-3321 (2012).
   
6. C. Tian et al., "ff19SB: Amino-Acid-Specific Protein Backbone Parameters Trained against Quantum Mechanics Energy Surfaces in Solution." *J Chem Theory Comput*, 16, 528-552 (2020).
   
7. N. T. Pierce, L. Irber, T. Reiter, P. Brooks, C. T. Brown, "Large-scale sequence comparisons with sourmash." *F1000Res*, 8, 1006 (2019).

8. H. Müller, H.-P. Kley, "Retrospective study on the reliability of an 'approximate LD<SUB>50</SUB>' determined with a small number of animals." *Archives of Toxicology*, 51, 189-196 (1982).
   
9. E. Kugelberg et al., "Establishment of a superficial skin infection model in mice by using Staphylococcus aureus and Streptococcus pyogenes." *Antimicrobial Agents and Chemotherapy*, 49, 3435-3441 (2005).
   
10. H. K. Kim, D. Missiakas, O. Schneewind, "Mouse models for infectious diseases caused by Staphylococcus aureus." *J Immunol Methods*, 410, 88-99 (2014).
   
11. A. Six et al., "Pyocin efficacy in a murine model of Pseudomonas aeruginosa sepsis." *J Antimicrob Chemother*, 76, 2317-2324 (2021).
   
12. A. Chiba, S. Sugimoto, F. Sato, S. Hori, Y. Mizunoe, "A refined technique for extraction of extracellular matrices from bacterial biofilms and its applicability." *Microbial Biotechnology*, 8, 392-403 (2015).
   
13. S. Tyanova, T. Temu, J. Cox, "The MaxQuant computational platform for mass spectrometry-based shotgun proteomics." *Nature Protocols*, 11, 2301-2319 (2016).
   
14. M. S. Bolhuis et al., "Synergy between linezolid and clarithromycin against." *Eur Respir J*, 44, 808-811 (2014).

# Bacteriophage-inspired Targeting Sites of HU

Supplementary figure 1: Bacteriophage-inspired targeting sites of HU.  
(A-B) The structural formulas of SD1, SD4, and BDF.  
(C) The proposed targeting sites for BDFs and SDs indicated by the red arrows. The arms, pit, and the α-helical regions of Apo SaHU (PDB ID: 4QJN) are colored in silver, olive, and cyan, respectively.  
(D) The Gp46-HBsu complex with interface 1 (site 1) and interface 2 (site 2) indicated by circles.  
(E) Multiple sequence alignment of representative bacteria - B. subtilis (Bs), S. aureus (Sa), M. tuberculosis (Mt), S. pneumoniae (Sn), S. pyogenes (Sp), and A. baumannii (Ab) by ClustalOmega.  
(F) Two representative molecules docked on site 1 and 2, using the sites shown in (D) and (E). The residues that are key for the interactions are highlighted in purple and numbered.  
(G-H) The cartoon illustration of top 10 drugs from DrugBank for site 1 (G) and site 2 (H).  

- Bisphenol derivative of fluorene (BDF)  
- Trans-stilbene derivative (SD1)  
- Trans-stilbene derivative (SD4)

## Supplementary Figure 2: Belinostat Interaction with Histone-Like Proteins (HUs) and Growth Inhibition in B. subtilis

(A) 1D NMR WaterLOGSY spectra of Belinostat:
- Belinostat (black)
- Belinostat with HUs from:
  - A. baumannii (lime)
  - S. pneumoniae (orange)
  - B. subtilis (yellow)
  - M. tuberculosis (purple)
  - S. pyogenes (green)
  - S. aureus (red)

(B) Minimum inhibitory concentrations (MICs) of Belinostat on B. subtilis strains (ATCC 6051 and 168).

(C) Belinostat does not have an inhibitory effect on P. aeruginosa.

| Bacteria        | Belinostat     |
|-----------------|----------------|
| B. subtilis     |                |
| Belinostat      |                |
| S. pyogenes     |                |
| S. pneumoniae   |                |
| B. subtilis     |                |
| M. tuberculosis |                |
| A. baumannii    |                |
| 1H              |                |
| S. aureus       |                |
| C               |                |
| P. aeruginosa   |                |

## Supplementary Figure 3: Lead Compound Library Expansion and Verification Among HDAC Inhibitors

(A) The structural formulas of Panobinostat and the top three optimized molecules from PGMO.  
(B) Calculation of MIC for Panobinostat on S. aureus.  
(C) ASTs for Belinostat, Panobinostat, Vorinostat, Pracinostat, and Dacinostat. 200 µg of each drug dissolved in 20 µL of DMSO was loaded on each plate.  
(D) 1D NMR WaterLOGSY spectra show no interaction between Vorinostat and SaHU.  
(E) Vorinostat shows no inhibitory effect at 660 µg/mL (2.5 mM) for S. aureus.

### Chemical Compounds:
- Panobinostat
- Belinostat
- Vorinostat
- Pracinostat
- Dacinostat

### Concentration:
- DMSO 2.5 mM

### NMR Spectra Peaks:
- Aliphatic region
- Aromatic region
- 1H (ppm)

### Interaction Analysis:
- Vorinostat + SaHU

Please let me know if you need any further refinement or clarification.

## DMSO
- R4Cl
- R4F
- R24Cl
- R4Br

## A
- C
- R4Cl
- R24Cl

## B
Supplementary figure 4: Lead compound library expansion and verification among CHADs.
(A) ASTs for R4Cl, R24Cl R4F, R4Br, and CHA. 200 µg of each small molecule dissolved in 20 µL of DMSO was loaded on each plate. 
(B) The MIC determinations for R4Cl and R24Cl on S. aureus. 
(C) The MIC determinations for R4F and R4Br on S. aureus. 
(D) The MIC determination for CHA on S. aureus. 
(E) The binding affinity between CHA and SaHU determined by MST.

- R4Br
- R4F
- D
- CHA
- DMSO
- CHA
- E

KD = 5.77 ±0.93 µM

## Supplementary Figure 5: Additional CHADs with Possible Antibacterial Properties 

(A) Additional small molecules from ZINC20 with substitutions on R4 group of CHA. 
(B) Additional small molecules from ZINC20 with substitutions on R3 group of CHA.

# Cinnamic Acid

**Supplementary Figure 6:** Cinnamic acid has no antibacterial activity against *S. aureus*.

(A) AST for cinnamic acid in comparison with CHA and R4Cl. 200 µg of each small molecule dissolved in 20 µL of DMSO was loaded on each plate.

(B) The MIC determination for cinnamic acid on *S. aureus*.

### Supplementary figure 7: NMR studies of SaHU-CHADs interactions

(A) Peak intensity changes for each residue after adding Panobinostat (dash line indicates 50% mark).

(B) Overlay of 1H-15N HSQC spectra of SaHUD15G (black) and SaHUD15G with 5 molar equivalents of R4Cl added (red).

(C) Peak intensity changes for each residue after adding R4Cl (dash line indicates 70% mark).

(D) Overlay of 1H-15N HSQC spectra of SaHUD15G (black) and SaHUD15G with 5 molar equivalents of CHA added (red). The similar set of residues experienced chemical perturbations or peak broadening as seen in Panobinostat titration.

#### HU
- R4Cl = 1 : 5
- CHA = 1 : 5

#### Residues:
- N2
- E51
- V52
- K18
- V42
- E54
- G48
- G39
- A64
- Q43
- R53

### Supplementary Figure 8: Free Energy Calculation and RBFE

(A) The total energy contribution per residue. The arrows point to the two valleys in which the corresponding residues contribute most to the binding free energy. 

(B) Two valleys are highlighted on the structure of SaHUD15G with corresponding residues labeled. 

(C) The linear correlation between calculated RBFEs (ΔΔG) and the experimentally determined MICs with Panobinostat as the only outlier. 

C

G48

### Supplementary Figure 9: Antibiotic-resistant and Genomic Sequence Profiles of 50 MRSA Strains

(A) The antibiotic resistant profiles of clinically isolated MRSA:
- A-Clindamycin
- B-Daptomycin
- C-Erythromycin
- D-Gentamicin
- E-Linezolid
- F-Levofloxacin
- G-Moxifloxacin
- H-Oxacillin
- I-Penicillin
- J-Rifampin
- K-Sulfamethoxazole
- L-Teicoplanin
- M-Tigecycline
- N-Vancomycin

Bar: 
- 1.0-Sensitive
- 2.0-Intermediate
- 3.0-Resistant

(B) Heatmap and dendrogram established from 50 genomes of MRSA using Sourmash "signatures". Full matrix with rows and columns clustering 50 MRSA strains organized by their sequence similarity and MRSA-43 representing an outgroup.

![Supplementary Figure 9](insert_image_link_here)

## Control
- Panobinostat
- R4Cl
- Belinostat
- Heart
- Liver
- Spleen
- Lung
- Kidney

![Supplementary figure 10](image_link_here)

Toxicity of Belinostat, Panobinostat, and R4Cl in mice via superficial application. 

Gross autopsy of heart, liver, spleen, lungs, and kidneys.

## Belinostat

| Seq. | Dosage (mg/kg) | Short-term outcome | Long-term outcome | Symptoms                         |
|------|-----------------|--------------------|-------------------|----------------------------------|
| 1    | 175             | O                  | O                 | Shortness of breath, weakness, recovered after 1 hour, be dissected 14 days later  |
| 2    | 280             | X                  | X                 | Severe tremor, weakness, dead after 5 min                                       |
| 3    | 175             | O                  | O                 | Weakness, recovered after 2 hours, be dissected 14 days later                    |
| 4    | 280             | X                  | X                 | Severe tremor, weakness, dead after 5 min                                       |
| 5    | 175             | O                  | O                 | Tremor, weakness, recovered after 2 hours, be dissected 14 days later           |

Belinostat (X = Died, O = Survived)

Stopping criteria met: LR criterion

Estimated LD50 = 242.7 (Based on an assumed sigma of 0.2)

Approximate 95% confidence interval is 175 to 280.

## Panobinostat

| Seq. | Dosage (mg/kg) | Short-term outcome | Long-term outcome | Symptoms                         |
|------|-----------------|--------------------|-------------------|----------------------------------|
| 1    | 175             | O                  | O                 | Shortness of breath, weakness, recovered after 4 hours, be dissected 14 days later |
| 2    | 280             | X                  | X                 | Tremor, weakness, dead after 5 min                                             |
| 3    | 175             | O                  | O                 | Weakness, recovered after 2 h, be dissected 14 days later                         |
| 4    | 280             | X                  | X                 | Tremor, weakness, dead after 5 min                                             |
| 5    | 175             | O                  | O                 | Weakness, recovered after 2 h, be dissected 14 days later                         |

Panobinostat (X = Died, O = Survived)

Stopping criteria met: LR criterion

Estimated LD50 = 78.64 (Based on an assumed sigma of 0.2)

Approximate 95% confidence interval is 70 to 110.

## R4Cl

| Seq. | Dosage (mg/kg) | Short-term outcome | Long-term outcome | Symptoms                         |
|------|-----------------|--------------------|-------------------|----------------------------------|
| 1    | 175             | O                  | O                 | Shortness of breath, weakness, recovered after 4 hours, be dissected 14 days later |
| 2    | 280             | X                  | X                 | Tremor, weakness, dead after 5 min                                             |
| 3    | 175             | O                  | O                 | Weakness, recovered after 2 h, be dissected 14 days later                         |
| 4    | 280             | X                  | X                 | Tremor, weakness, dead after 5 min                                             |
| 5    | 175             | O                  | O                 | Weakness, recovered after 2 h, be dissected 14 days later                         |

R4Cl (X = Died, O = Survived)

Stopping criteria met: LR criterion

Estimated LD50 = 242.7 (Based on an assumed sigma of 0.2)

Approximate 95% confidence interval is 175 to 280.

Supplementary figure 11: The acute toxicity tests for intravenous injection of Belinostat, Panobinostat and R4Cl. LD50 for Belinostat (A), Panobinostat (B) and R4Cl (C) were determined using the up-and-down procedure.

## Supplementary Figure 12

The 7 days toxicity tests for intravenous injection of Belinostat, Panobinostat, and R4Cl in mice.

### (A) Organ Indices
- The heart, liver, spleen, lung, and kidney indices.
- Organ index (mg/g) = organ weight (mg) / body weight of mice (g) (n = 6).

### (B) Cell Counts or Percentages
- WBCs, Neu, Lym, PLT, RBCs, and HGB in different groups (n = 6).
- Statistics: two-tailed t test. 
- Mean with SD. 
- ns, not significant; *, p < 0.05; **, p < 0.01; ***, p < 0.001.

|   | Control | R4Cl | Belinosta | Panobinostat |
|---|---------|------|-----------|--------------|
| 0.0 | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 |
| Neu (10^9/L) | ns | ** | * |

|   | Control | R4Cl | Belinosta | Panobinostat |
|---|---------|------|-----------|--------------|
| 0.0 | 0.5 | 1.0 | 1.5 | 2.0 |
| Lym (10^9/L) | ns | **** | ******** |

# Bacteria MIC (μg/mL)
| Bacteria             | Tobramycin | Erythromycin | Rifamycin |
|----------------------|------------|--------------|-----------|
| B. subtilis (168)    | 0.5        | -            | -         |
| S. aureus (ATCC 29213) | 0.5       | -            | -         |
| A. baumannii (BBA-1605) | -        | 6            | -         |
| E. coli (MG1655)     | -          | 4            | -         |
| K. pneumonia (ATCC 13883) | -      | 4            | -         |
| P. aeruginosa (PAO1) | -          | 1            | -         |
| M. Tuberculosis (H37Rv) | -        | -            | 0.25      |

**Supplementary figure 13: Survival curves and quality controls.**
(A) Kaplan-Meier survival curves (n = 10) of the solvent used in this study (untreated) and Belinostat (treated) injected P. aeruginosa sepsis mice that monitored for 48 hours. 
(B) The quality controls of the bacteria used in the study: tobramycin for Gram-positive bacteria (except for M. tuberculosis), erythromycin for Gram-negative bacteria, and Rifamycin for M. tuberculosis.

## Marker
- Cellular
- Material
- Medium
- Biofilm

## S. aureus
- S. aureus + R4Cl

## Marker
- Cellular
- Material
- Medium
- Biofilm

## Molecular Weights
- 10 kDa
- 15 kDa
- 20 kDa
- 25 kDa
- 37 kDa
- 50 kDa
- 75 kDa
- 100 kDa

![Supplementary figure 14: SDS-PAGE image showing the protein contents of different fractions of S. aureus. The gel image showing the protein content of cell lysate, medium and biofilm with and without R4Cl treatment.](image_link_here)

```
## Pathways
- beta-Lactam resistance
- Purine metabolism
- Microbial metabolism in diverse environments
- Pentose phosphate pathway
- Sulfur metabolism
- Selenocompound metabolism
- Methane metabolism
- Oxidative phosphorylation
- Biosynthesis of secondary metabolites
- Glycolysis / Gluconeogenesis
- Lysine degradation
- Nucleotide excision repair
- Alanine, aspartate and glutamate metabolism
- Carbon metabolism
- Ribosome
- Glyoxylate and dicarboxylate metabolism
- Starch and sucrose metabolism
- O-Antigen nucleotide sugar biosynthesis
- Cyanoamino acid metabolism
- Glycerophospholipid metabolism

## Supplementary Figure 15
### The effect of R4Cl on E. coli
- Growth curve of E. coli and E. coli treated with 10 µg/mL of R4Cl over 24 hours.
- Gram staining images showing no difference between E. coli and E. coli treated with 10 µg/mL of R4Cl.
- KEGG pathway enrichment analysis of differentially expressed genes between 10 µg/mL of R4Cl treated and untreated E. coli cells. 
  - Y-axis indicates the pathway name, x-axis indicates gene ratio. The bubble size indicates the number of genes and the color bar indicates the adjusted p-value.

![E. coli vs. E. coli treated with R4Cl](image_link)

### Growth Curve
Time (hour) | OD600
--- | ---
0 | 0.0
4 | 0.5
8 | 1.0
12 | 1.5
16 | 2.0
20 | 2.5
24 | 3.0

```
Please replace "image_link" with the actual link to the image showing E. coli vs. E. coli treated with R4Cl.
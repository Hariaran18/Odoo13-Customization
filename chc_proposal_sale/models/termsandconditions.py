from odoo import models, fields, api

class terms_Conditions(models.Model):
    _name = "terms.conditions"

    name= fields.Char(string="Terms and Conditions", default="General")

    terms_conditions1a_proposal = fields.Text(string="Land Area", default="The Customer shall make an available land area measuring approximately 1.0 acre per Dry batching plant for the whole duration of the entire project. The land must be approximately leveled, compacted and accessible to Chin Hin Concrete’s Mixer Trucks and Suppliers to the batching plant. Contractor or developer shall provide proper access road for the delivery of concrete to the point of discharge without any charges.")
    terms_conditions1b_proposal = fields.Text(string="Land Condition", default="The Developer or Customer shall make available land without cost for the whole duration of the entire project. The land provided preferably to be rectangular in shape for each concrete plants and stockpile of raw materials. The land condition shall be without any debris, rubbish and any waste materials.The Developer shall not allow any of its sub-contractors working on the Project or any other party to set up any concrete batching plants on the site of the Project. The Developer shall by way of written notification to the sub-contractors for the project, requiring them to obtain its supplies of concrete for the Project from Chin Hin Concrete.")
    terms_conditions1c_proposal = fields.Text(string="Plant", default="Chin Hin Concrete shall undertake to supply with the option erect and commission one (1) number on-site concrete Dry Batching Plant")

    terms_conditions2a_proposal = fields.Text(string="Condition 2a", default="Truck allocation is based on development site concrete demand, ratio per truck to serve is about 650m3 per truck.")
    trucks_assigned1_proposal = fields.Text(string="Truck Assigned1", default="5-7")
    trucks_assigned2_proposal = fields.Text(string="Trucks Assigned2", default="8-10")
    monthly_m3a_proposal = fields.Text(string="Monthly m3(1)",default="4500")
    monthly_m3b_proposal = fields.Text(string="Monthly m3(2)", default="6000")

    terms_conditions3a_proposal = fields.Text(string="Condition 3a", default="[customer name] shall not allow any of its sub-contractors working on the Project or any other party to set up any concrete batching plants on the site of the Project. [customer name] shall by way of written notification to the sub-contractors for the project, requiring them to obtain its supplies of concrete for the Project from CHIN HIN CONCRETE (KL) SDN BHD.")
    terms_conditions3b_proposal = fields.Text(string="Condition 3b", default="In the event Chin Hin Concrete (KL) Sdn Bhd main site batching plant is unable to supply, Chin Hin Concrete (KL) will supply from its external Ready Mixed Concrete Plant as a backup batching plant.")
    terms_conditions3c_proposal = fields.Text(string="Condition 3c", default="We shall be responsible for the delivery of concrete up to the project site at all reasonable time.")

    terms_conditions4a_proposal = fields.Text(string="Condition 4a", default="All of the concrete volume must be assigned to Chin Hin Concrete (KL) Sdn Bhd.")
    terms_conditions4b_proposal = fields.Text(string="Condition 4b", default="Chin Hin Concrete (KL) Sdn Bhd batching plant is allowed to stay without relocation in the period of at least Thirty-Six (36) months or until the completion of major structure.")
    terms_conditions4c_proposal = fields.Text(string="Condition 4c", default="A one (1) month notice must be given to CHIN HIN CONCRETE (KL) SDN BHD by [customer name] before relocation/demobilisation of batching plant.")

    terms_conditions5a_proposal = fields.Text(string="Condition 5a", default="Price are subject to price fluctuation in the cost of direct materials and other direct costs in production of concrete shall necessitate or adjustment in concrete prices accordingly.")

    terms_conditions6a_proposal = fields.Text(string="Condition 6a", default="Endeavour to assist in the application of water, electricity from relevant authorities. CHIN HIN CONCRETE (KL) SDN BHD shall make available electricity and water the boundary of the allocated land for the Batching Plant for its operation. Chin Hin Concrete (KL) Sdn Bhd shall bear all periodic consumption charges from the operations of the batching plant only.")

    terms_conditions7a_proposal = fields.Text(string="Condition 7a", default="CHIN HIN CONCRETE (KL) SDN BHD batching plant is designed to minimize the generation of waste. Waste generated shall be collected in a pit, which acts as a sediment pond.  Solid waste is separated from the liquid waste through process settlement in the pit. The solid waste shall be allowed to dry and then dispose off.")

    terms_conditions8a_proposal = fields.Text(strng="Condition 8a", default="Chin Hin Concrete (KL) Sdn Bhd will supply to the said development on a first priority basis and allow to sell concrete outside the said development when internal demand of concrete is low. (Below 4,500m3 per month)")

    terms_conditions9a_proposal = fields.Text(string="Condition 9a", default="The quantity of delivered concrete shall be based on the delivery docket.")
    terms_conditions9b_proposal = fields.Text(string="Condition 9b", default="If you have doubts as to the quantity of concrete delivered, your written complaint must reach us within three (3) days from the date of delivery. Otherwise, the quantity of concrete supplied/delivered detailed in our delivery docket(s) shall be deemed to be correct.")
    terms_conditions9c_proposal = fields.Text(string="Condition 9c", default="In the event of dispute, the quantity delivered shall be determined by a joint measurement at site conducted by both parties. A variation tolerance shall be allowed in the calculation of volume, and it shall be as follows:-")
    structure1_proposal = fields.Text(string="Structure Val1",default="Columns")
    structure2_proposal = fields.Text(string="Structure Val2", default="Formed Slabs")
    structure3_proposal = fields.Text(string="Structure Val3", default="Ground Slabs/Ground Structure (exclude bored pile)")
    variation1_proposal = fields.Text(string="Variation Val1",default="±5%")
    variation2_proposal = fields.Text(string="Variation Val2", default="±3%")
    variation3_proposal = fields.Text(string="Variation Val3", default="±13%")


    terms_conditions10a_proposal = fields.Text(string="Condition 10a", default="Concrete compressive strength shall be determined based on respective cube test result(s) only of the concrete supplied, provided that BS1881:1983/EN1230:2019 for the specification of concrete handling and testing are adhered to. Compliance to characteristic strength shall follow the relevant clauses stipulated in MS523/BS5328.")
    terms_conditions10b_proposal = fields.Text(string="Condition 10b", default="In the event you intend to engage an independent laboratory to conduct any technical tests on the concrete, the independent laboratory must be endorsed by us and such test(s) is conducted at your costs. A copy of the test(s) report shall be given to us within 7 days of testing or the result, whichever that is earlier.")
    terms_conditions10c_proposal = fields.Text(string="Condition 10c", default="We will not be responsible for concrete failures or rejects as a result of: ")
    terms_conditions10c1_proposal = fields.Text(string="Condition 10c1", default="Additional of water or admixture and/or any form of adulterations to the concrete by you and/or your site personnel after discharge from the mixer trucks.")
    terms_conditions10c2_proposal = fields.Text(string="Condition 10c2", default="Poor placement method and/or inadequate/poor handling at your work site (including but not limited to inconsistency of concrete placing, uneven compaction and/or unskilled workmanship).")
    terms_conditions10c3_proposal = fields.Text(string="Condition 10c3", default="Delay in placement time beyond 2 (two) hours after time of batching; and")
    terms_conditions10c4_proposal = fields.Text(string="Condition 10c4", default="Placing concrete at the site by you and/or other 3rd party when it is raining at the site.")
    terms_conditions10d_proposal = fields.Text(string="Condition 10d", default="Save and except as expressly provided herein and/or agreed by us in any written document(s) initiated from us, we make no other assurances, representations, guarantees, warranties or conditions on the concrete sold or supplied by us to you, whether express, implied, statutory or otherwise, including but not limited to the description, quality, merchantability and fitness for any particular purpose, and we hereby specifically disclaim any such assurances, representations, guarantees, warranties or conditions.")
    terms_conditions10e_proposal = fields.Text(string="Condition 10e", default="In the event that the concrete supplied by us is conclusively proven to be below specification/ defective, it is hereby unequivocally and unconditionally agreed between the parties that the extent of our liability shall be strictly limited to replacement of the defective concrete. In particular, we shall, subject strictly to Clause 10.6 and/or Clause 10.7 below (whichever applicable), replace such defective concrete with fresh concrete free of charge or, at our absolute/sole discretion, to compensate you up to a maximum sum equivalent to the price of such defective concrete (provided always that we shall not be held responsible for the removal and/or act of replacing any such defective concrete).")
    terms_conditions10f_proposal = fields.Text(string="Condition 10f", default="Any dispute on the strength of the concrete must be notified to us in writing within thirty (30) days from the date of our delivery, failure of which the concrete supplied shall be deemed to be of sufficient strength and no dispute and/or claim in respect of its strength shall be accepted/allowed.")
    terms_conditions10g_proposal = fields.Text(string="Condition 10g", default="Save and except for dispute in respect of concrete strength as expressly provided in Clause 10.6 above, any other dispute on non-compliance of the concrete must be notified to us in writing within three (3) days from the date of our delivery, failure of which the concrete supplied shall be deemed to be of satisfactory quality and no dispute and/or claim shall be accepted/allowed.")
    terms_conditions10h_proposal = fields.Text(string="Condition 10h", default="In the event of non-compliance with clause 10.6 and/or 10.7 above, you shall be deemed to have waived your right(s) to dispute and/or claim in respect of the concrete supplied to you by us.")

    terms_conditions11a_proposal = fields.Text(string="Condition 11a", default="Prices quoted include the costs for sampling and testing of the concrete at Chin Hin Concrete (KL) Sdn Bhd’s laboratory only. Chin Hin Concrete (KL) Sdn Bhd will not bear any of costs should the customer require additional testing of the concrete other than those carried out at our Chin Hin Concrete (KL) Sdn Bhd’s laboratory unless the customer has requested in writing and it is agreed by both parties (CHIN HIN CONCRETE (KL) SDN BHD and [customer name]. Proposed that the cube sampling and preparation to be done at the site laboratory to be set-up at the plant.")

    terms_conditions12a_proposal = fields.Text(string="Condition 12a", default="Chin Hin Concrete (KL) Sdn Bhd will be given a mobilization period of eight (08) weeks from the date of acceptance of this quotation and handing over of site possession for installation and commission of plant on site in normal circumstances.  And four weeks (4 weeks) to demobilization of plant when contract expire.")

    terms_conditions13a_proposal = fields.Text(string="Condition 113a", default="Chin Hin Concrete (KL) Sdn Bhd shall have the right to stop supply or terminate this agreement and shall not be responsible for any loss incurred by you due to the stoppage or termination in the event of any default in payment or breach of any other terms and conditions herein.  All losses and damages suffered by Chin Hin Concrete (KL) Sdn Bhd shall be liable by your Company.")
    terms_conditions13b_proposal = fields.Text(string="Condition 13b", default="Developer shall have the right to terminate the agreement should Chin Hin Concrete (KL) Sdn Bhd repeatedly unable to fulfill their obligation to supply.")

    terms_conditions14a_proposal = fields.Text(string="Condition 14a", default="The quotation is valid upon your acceptance within fourteen (14) days from the date appearing on our quotation letter.")

    terms_conditions15a_proposal = fields.Text(string="Condition 15a", default="Supply will commence upon approval of credit facility. Payment of concrete delivered and accepted in each monthly period shall be made strictly within sixty (60) days on the issuance of invoice by Chin Hin Concrete (KL) Sdn Bhd.  In default of payment or credit limit exceeded, Chin Hin Concrete (KL) Sdn Bhd reserve the right to immediately suspend the supply of concrete and credit facilities to the job without notice. Chin Hin Concrete (KL) Sdn Bhd will also reserve the right to recover such outstanding payments plus legal expenses and interest chargeable at the rate of 1.5% per month commencing from the due date.")

    terms_conditions16a_proposal = fields.Text(string="Condition 16a", default="Ordering")
    terms_conditions16a1_proposal = fields.Text(string="Condition 16a1", default="The Customer should give sufficient notice to Chin Hin Concrete (KL) Sdn Bhd for ordering and cancellation of concrete, preferably 24 hours. In the event Customer cancels the order after the concrete has been batched Customer shall bear the cost of the concrete and Chin Hin Concrete (KL) Sdn Bhd will bill Customer for the concrete batched. A levy of RM500.00 shall be payable to Chin Hin Concrete (KL) Sdn Bhd for any cancellation of order on Public Holidays or Sundays.")
    terms_conditions16b_proposal = fields.Text(string="Condition 16b", default="Delivery Order (DO)")
    terms_conditions16b1_proposal = fields.Text(string="Condition 16b1", default="In the event of any of the Delivery Order being misplaced or not signed by the contractor‘s site representative during the supply, Chin Hin Concrete (KL) Sdn Bhd reserves the right to invoice based on the total progress amount of the final confirmed quantity as shown on the Delivery Orders. In the events that D/O’s are not returned within 48 hours of the supply, Chin Hin Concrete (KL) Sdn Bhd reserves the right to suspend the delivery.")

    terms_conditions17a_proposal = fields.Text(string="Condition 17a", default="The performance of our obligation under our Tender/Quotation is subject to the effect thereon of Force Majeure, which shall include any event or occurrence beyond our reasonable control including but not limited to act of ‘God’, adverse weather condition, haze, enemy control, war (whether declared or not), terrorist attack or threat, acts of sabotage, civil commotion/strife or other labour disputes/disturbances, lock out, fire, accidents, quality and source of raw materials, breakdown of plant and/or equipment, lack or stoppage of supply and increase in costs of raw materials, and/or other cause or causes whether similar or dissimilar to those mentioned (“Force Majeure Conditions”) which is beyond our reasonable control.")
    terms_conditions17b_proposal = fields.Text(string="Condition 17b", default="We shall not be liable and/or considered in default and/or breach of agreement with you for any loss, liability, damage, cost or expenses caused by any of the Force Majeure Conditions.")

    terms_conditions18a_proposal = fields.Text(string="Condition 18a", default="Any notice, communication or demand shall be deemed to have been sufficiently given if sent by prepaid post to your address stated herein or to your last known place of business and shall be presumed to have reached your address in ordinary course of post. Any mode of communication by email, SMS and Whatsapp between the parties shall prima facie be admissible in Court with regard to its existence, and its contents being subject to proof.")
    terms_conditions18b_proposal = fields.Text(string="Condition 18b", default="In the event any of our cube mould(s) is lost misplaced or destroyed at your site and/or under your custody, a replacement cost shall be charged to you at RM150.00 per mould plus 6% of GST.")

    terms_conditions19a_proposal = fields.Text(string="Condition 19a", default="The developer shall assist to obtain all necessary support documents for plant application matters, in order for application process to setup batching plant. (i.e Quit land, Approved Development Order, Land Plan) Chin Hin Concrete will undertake to pay all fines by DOE or any local authorities due to violation and breach of any allocable law and regulations in so far as it relates to concrete batching plant at site.")

    terms_conditions20a_proposal = fields.Text(string="Condition 20a", default="The terms and conditions contained herein together with the respective Quotation from us shall not at any time be changed, varied and/or deleted by you without our prior written approval. In the event that your purchaser order(s), letter of award, contract(s) and/or any other documents shall contain any terms and conditions that differ from those contained herein, you hereby expressly acknowledge and agree that the terms and conditions contained herein together with the respective Quotation from us shall prevail to the extent of the conflict, and in the event the terms and conditions contained herein are more favorable to us.")

    terms_conditions21a_proposal = fields.Text(string="Condition 21a", default="This contract of supply and the terms and conditions herein shall be deemed agreed by you upon your signing on the acknowledgement/ Quotation overleaf or upon you placing your first purchase order subsequent to the date of this Quotation. This contract shall be construed in accordance with the Laws of Malaysia.")

    line_number_1 = fields.Text(string="Line No.1", default="1. Batching Plant")
    line_number_1a = fields.Text(string="Line No.1.1", default="1.1 Land Area")
    line_number_1b = fields.Text(string="Line No.1.2", default="1.2 Land Condition")
    line_number_1c = fields.Text(string="Line No.1.3", default="1.3 Plant")

    line_number_2 = fields.Text(string="Line No.2", default="2. Truck Allocation")
    line_number_2a = fields.Text(string="Line No.2.1", default="2.1")

    line_number_3 = fields.Text(string="Line No.3", default="3. Supply of Concrete")
    line_number_3a = fields.Text(string="Line No.3.1", default="3.1")
    line_number_3b = fields.Text(string="Line No.3.2", default="3.2")
    line_number_3c = fields.Text(string="Line No.3.3", default="3.3")

    line_number_4 = fields.Text(string="Line No.4", default="4. Volume & Duration")
    line_number_4a = fields.Text(string="Line No.4.1", default="4.1")
    line_number_4b = fields.Text(string="Line No.4.2", default="4.2")
    line_number_4c = fields.Text(string="Line No.4.3", default="4.3")

    line_number_5 = fields.Text(string="Line No.5", default="5. Variation of Price")
    line_number_5a = fields.Text(string="Line No.5.1", default="5.1")

    line_number_6 = fields.Text(string="Line No.6", default="6. Electricity & Water Supply")
    line_number_6a = fields.Text(string="Line No.6.1", default="6.1")

    line_number_7 = fields.Text(string="Line No.7", default="7. Waste Management")
    line_number_7a = fields.Text(string="Line No.7.1", default="7.1")

    line_number_8 = fields.Text(string="Line No.8", default="8. External Supply")
    line_number_8a = fields.Text(string="Line No.8.1", default="8.1")

    line_number_9 = fields.Text(string="Line No.9", default="9. Quantity Assurance")
    line_number_9a = fields.Text(string="Line No.9.1", default="9.1")
    line_number_9b = fields.Text(string="Line No.9.2", default="9.2")
    line_number_9c = fields.Text(string="Line No.9.3", default="9.3")

    line_number_10 = fields.Text(string="Line No.10", default="10. Quality Assurance")
    line_number_10a = fields.Text(string="Line No.10.1", default="10.1")
    line_number_10b = fields.Text(string="Line No.10.2", default="10.2")
    line_number_10c = fields.Text(string="Line No.10.3", default="10.3")
    line_number_10c1 = fields.Text(string="Line No.10.3.1", default="10.3.1")
    line_number_10c2 = fields.Text(string="Line No.10.3.2", default="10.3.2")
    line_number_10c3 = fields.Text(string="Line No.10.3.3", default="10.3.3")
    line_number_10c4 = fields.Text(string="Line No.10.3.4", default="10.3.4")
    line_number_10d = fields.Text(string="Line No.10.4", default="10.4")
    line_number_10e = fields.Text(string="Line No.10.5", default="10.5")
    line_number_10f = fields.Text(string="Line No.10.6", default="10.6")
    line_number_10g = fields.Text(string="Line No.10.7", default="10.7")
    line_number_10h = fields.Text(string="Line No.10.8", default="10.8")

    line_number_11 = fields.Text(string="Line No.11", default="11. Concrete Sampling and Cube Testing")
    line_number_11a = fields.Text(string="Line No.11.1", default="11.1")

    line_number_12 = fields.Text(string="Line No.12", default="12. Mobilization & Demobilization if Batching Plant")
    line_number_12a = fields.Text(string="Line No.12.1", default="12.1")

    line_number_13 = fields.Text(string="Line No.13", default="13. Termination")
    line_number_13a = fields.Text(string="Line No.13.1", default="13.1")
    line_number_13b = fields.Text(string="Line No.13.2", default="13.2")

    line_number_14 = fields.Text(string="Line No.14", default="14. Validity of Quotation")
    line_number_14a = fields.Text(string="Line No.14.1", default="14.1")

    line_number_15 = fields.Text(string="Line No.15", default="15. Payment Terms")
    line_number_15a = fields.Text(string="Line No.15.1", default="15.1")

    line_number_16 = fields.Text(string="Line No.16", default="15. Ordering and Delivery Order")
    line_number_16a = fields.Text(string="Line No.16.1", default="16.1")
    line_number_16a1 = fields.Text(string="Line No.16.1.1", default="16.1.1")
    line_number_16b = fields.Text(string="Line No.16.2", default="16.2")
    line_number_16b1 = fields.Text(string="Line No.16.2.1", default="16.2.1")

    line_number_17 = fields.Text(string="Line No.17", default="17. Force Majeure")
    line_number_17a = fields.Text(string="Line No.17.1", default="17.1")
    line_number_17b = fields.Text(string="Line No.17.2", default="17.2")

    line_number_18 = fields.Text(string="Line No.18", default="18. Notices")
    line_number_18a = fields.Text(string="Line No.18.1", default="18.1")
    line_number_18b = fields.Text(string="Line No.18.2", default="18.2")

    line_number_19 = fields.Text(string="Line No.19", default="19. Others")
    line_number_19a = fields.Text(string="Line No.19.1", default="19.1")

    line_number_20 = fields.Text(string="Line No.20", default="20. Application of Terms and Conditions")
    line_number_20a = fields.Text(string="Line No.20.1", default="20.1")

    line_number_21 = fields.Text(string="Line No.21", default="21. Governing Law")
    line_number_21a = fields.Text(string="Line No.21.1", default="21.1")

    terms_conditions_ud1 = fields.Text(string="Line No.22")
    terms_conditions_ud2 = fields.Text(string="Line No.23")
    terms_conditions_ud3 = fields.Text(string="Line No.24")
    terms_conditions_ud4 = fields.Text(string="Line No.25")
    terms_conditions_ud5 = fields.Text(string="Line No.26")








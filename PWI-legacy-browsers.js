/************ 
 * Pwi *
 ************/


// store info about the experiment session:
let expName = 'PWI';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.9922, 0.9608, 0.8902]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(blank500RoutineBegin());
flowScheduler.add(blank500RoutineEachFrame());
flowScheduler.add(blank500RoutineEnd());
flowScheduler.add(familiarIntroRoutineBegin());
flowScheduler.add(familiarIntroRoutineEachFrame());
flowScheduler.add(familiarIntroRoutineEnd());
flowScheduler.add(blank500RoutineBegin());
flowScheduler.add(blank500RoutineEachFrame());
flowScheduler.add(blank500RoutineEnd());
flowScheduler.add(NamingIntroRoutineBegin());
flowScheduler.add(NamingIntroRoutineEachFrame());
flowScheduler.add(NamingIntroRoutineEnd());
flowScheduler.add(blank500RoutineBegin());
flowScheduler.add(blank500RoutineEachFrame());
flowScheduler.add(blank500RoutineEnd());
flowScheduler.add(practiceTrialInstructionsRoutineBegin());
flowScheduler.add(practiceTrialInstructionsRoutineEachFrame());
flowScheduler.add(practiceTrialInstructionsRoutineEnd());
flowScheduler.add(blank500RoutineBegin());
flowScheduler.add(blank500RoutineEachFrame());
flowScheduler.add(blank500RoutineEnd());
flowScheduler.add(TrialInstructionsRoutineBegin());
flowScheduler.add(TrialInstructionsRoutineEachFrame());
flowScheduler.add(TrialInstructionsRoutineEnd());
const Trial_1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Trial_1LoopBegin(Trial_1LoopScheduler));
flowScheduler.add(Trial_1LoopScheduler);
flowScheduler.add(Trial_1LoopEnd);



flowScheduler.add(betweentrialbreakRoutineBegin());
flowScheduler.add(betweentrialbreakRoutineEachFrame());
flowScheduler.add(betweentrialbreakRoutineEnd());
flowScheduler.add(NewSetBeginRoutineBegin());
flowScheduler.add(NewSetBeginRoutineEachFrame());
flowScheduler.add(NewSetBeginRoutineEnd());
const Trial_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Trial_2LoopBegin(Trial_2LoopScheduler));
flowScheduler.add(Trial_2LoopScheduler);
flowScheduler.add(Trial_2LoopEnd);



flowScheduler.add(betweentrialbreakRoutineBegin());
flowScheduler.add(betweentrialbreakRoutineEachFrame());
flowScheduler.add(betweentrialbreakRoutineEnd());
flowScheduler.add(NewSetBeginRoutineBegin());
flowScheduler.add(NewSetBeginRoutineEachFrame());
flowScheduler.add(NewSetBeginRoutineEnd());
const Trial_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Trial_3LoopBegin(Trial_3LoopScheduler));
flowScheduler.add(Trial_3LoopScheduler);
flowScheduler.add(Trial_3LoopEnd);



flowScheduler.add(betweentrialbreakRoutineBegin());
flowScheduler.add(betweentrialbreakRoutineEachFrame());
flowScheduler.add(betweentrialbreakRoutineEnd());
flowScheduler.add(NewSetBeginRoutineBegin());
flowScheduler.add(NewSetBeginRoutineEachFrame());
flowScheduler.add(NewSetBeginRoutineEnd());
const Trial_4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Trial_4LoopBegin(Trial_4LoopScheduler));
flowScheduler.add(Trial_4LoopScheduler);
flowScheduler.add(Trial_4LoopEnd);



flowScheduler.add(goodbyeRoutineBegin());
flowScheduler.add(goodbyeRoutineEachFrame());
flowScheduler.add(goodbyeRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'exp_items_s1.csv', 'path': 'exp_items_s1.csv'},
    {'name': 'image/tortoiseID_posSOA.png', 'path': 'image/tortoiseID_posSOA.png'},
    {'name': 'image/tortoiseID_posSOA2.png', 'path': 'image/tortoiseID_posSOA2.png'},
    {'name': 'image/dagger_NEU.png', 'path': 'image/dagger_NEU.png'},
    {'name': 'image/dagger_NEU2.png', 'path': 'image/dagger_NEU2.png'},
    {'name': 'image/legID_negSOA.png', 'path': 'image/legID_negSOA.png'},
    {'name': 'image/legID_negSOA2.png', 'path': 'image/legID_negSOA2.png'},
    {'name': 'image/sword_REL.png', 'path': 'image/sword_REL.png'},
    {'name': 'image/sword_REL2.png', 'path': 'image/sword_REL2.png'},
    {'name': 'image/nose_ID.png', 'path': 'image/nose_ID.png'},
    {'name': 'image/nose_ID2.png', 'path': 'image/nose_ID2.png'},
    {'name': 'image/castleNEU_posSOA.png', 'path': 'image/castleNEU_posSOA.png'},
    {'name': 'image/castleNEU_posSOA2.png', 'path': 'image/castleNEU_posSOA2.png'},
    {'name': 'image/noseREL_negSOA.png', 'path': 'image/noseREL_negSOA.png'},
    {'name': 'image/noseREL_negSOA2.png', 'path': 'image/noseREL_negSOA2.png'},
    {'name': 'image/deer_ID.png', 'path': 'image/deer_ID.png'},
    {'name': 'image/deer_ID2.png', 'path': 'image/deer_ID2.png'},
    {'name': 'image/planeREL_posSOA.png', 'path': 'image/planeREL_posSOA.png'},
    {'name': 'image/planeREL_posSOA2.png', 'path': 'image/planeREL_posSOA2.png'},
    {'name': 'image/swordNEU_negSOA.png', 'path': 'image/swordNEU_negSOA.png'},
    {'name': 'image/swordNEU_negSOA2.png', 'path': 'image/swordNEU_negSOA2.png'},
    {'name': 'image/trainUNREL_negSOA.png', 'path': 'image/trainUNREL_negSOA.png'},
    {'name': 'image/trainUNREL_negSOA2.png', 'path': 'image/trainUNREL_negSOA2.png'},
    {'name': 'image/skirtUNREL_posSOA.png', 'path': 'image/skirtUNREL_posSOA.png'},
    {'name': 'image/skirtUNREL_posSOA2.png', 'path': 'image/skirtUNREL_posSOA2.png'},
    {'name': 'image/rabbit_UNREL.png', 'path': 'image/rabbit_UNREL.png'},
    {'name': 'image/rabbit_UNREL2.png', 'path': 'image/rabbit_UNREL2.png'},
    {'name': 'image/windmillREL_negSOA.png', 'path': 'image/windmillREL_negSOA.png'},
    {'name': 'image/windmillREL_negSOA2.png', 'path': 'image/windmillREL_negSOA2.png'},
    {'name': 'image/tableREL_posSOA.png', 'path': 'image/tableREL_posSOA.png'},
    {'name': 'image/tableREL_posSOA2.png', 'path': 'image/tableREL_posSOA2.png'},
    {'name': 'image/windmillNEU_negSOA.png', 'path': 'image/windmillNEU_negSOA.png'},
    {'name': 'image/windmillNEU_negSOA2.png', 'path': 'image/windmillNEU_negSOA2.png'},
    {'name': 'image/plateUNREL_posSOA.png', 'path': 'image/plateUNREL_posSOA.png'},
    {'name': 'image/plateUNREL_posSOA2.png', 'path': 'image/plateUNREL_posSOA2.png'},
    {'name': 'image/glassID_negSOA.png', 'path': 'image/glassID_negSOA.png'},
    {'name': 'image/glassID_negSOA2.png', 'path': 'image/glassID_negSOA2.png'},
    {'name': 'image/castleUNREL_negSOA.png', 'path': 'image/castleUNREL_negSOA.png'},
    {'name': 'image/castleUNREL_negSOA2.png', 'path': 'image/castleUNREL_negSOA2.png'},
    {'name': 'image/legID_posSOA.png', 'path': 'image/legID_posSOA.png'},
    {'name': 'image/legID_posSOA2.png', 'path': 'image/legID_posSOA2.png'},
    {'name': 'image/churchNEU_negSOA.png', 'path': 'image/churchNEU_negSOA.png'},
    {'name': 'image/churchNEU_negSOA2.png', 'path': 'image/churchNEU_negSOA2.png'},
    {'name': 'image/legUNREL_posSOA.png', 'path': 'image/legUNREL_posSOA.png'},
    {'name': 'image/legUNREL_posSOA2.png', 'path': 'image/legUNREL_posSOA2.png'},
    {'name': 'image/noseREL_posSOA.png', 'path': 'image/noseREL_posSOA.png'},
    {'name': 'image/noseREL_posSOA2.png', 'path': 'image/noseREL_posSOA2.png'},
    {'name': 'image/armNEU_negSOA.png', 'path': 'image/armNEU_negSOA.png'},
    {'name': 'image/armNEU_negSOA2.png', 'path': 'image/armNEU_negSOA2.png'},
    {'name': 'image/tortoiseUNREL_posSOA.png', 'path': 'image/tortoiseUNREL_posSOA.png'},
    {'name': 'image/tortoiseUNREL_posSOA2.png', 'path': 'image/tortoiseUNREL_posSOA2.png'},
    {'name': 'image/swan_REL.png', 'path': 'image/swan_REL.png'},
    {'name': 'image/swan_REL2.png', 'path': 'image/swan_REL2.png'},
    {'name': 'image/coatUNREL_posSOA.png', 'path': 'image/coatUNREL_posSOA.png'},
    {'name': 'image/coatUNREL_posSOA2.png', 'path': 'image/coatUNREL_posSOA2.png'},
    {'name': 'image/windmillID_negSOA.png', 'path': 'image/windmillID_negSOA.png'},
    {'name': 'image/windmillID_negSOA2.png', 'path': 'image/windmillID_negSOA2.png'},
    {'name': 'image/tableID_posSOA.png', 'path': 'image/tableID_posSOA.png'},
    {'name': 'image/tableID_posSOA2.png', 'path': 'image/tableID_posSOA2.png'},
    {'name': 'image/armREL_posSOA.png', 'path': 'image/armREL_posSOA.png'},
    {'name': 'image/armREL_posSOA2.png', 'path': 'image/armREL_posSOA2.png'},
    {'name': 'image/bedNEU_negSOA.png', 'path': 'image/bedNEU_negSOA.png'},
    {'name': 'image/bedNEU_negSOA2.png', 'path': 'image/bedNEU_negSOA2.png'},
    {'name': 'image/legUNREL_negSOA.png', 'path': 'image/legUNREL_negSOA.png'},
    {'name': 'image/legUNREL_negSOA2.png', 'path': 'image/legUNREL_negSOA2.png'},
    {'name': 'image/wardrobeREL_negSOA.png', 'path': 'image/wardrobeREL_negSOA.png'},
    {'name': 'image/wardrobeREL_negSOA2.png', 'path': 'image/wardrobeREL_negSOA2.png'},
    {'name': 'image/deerUNREL_negSOA.png', 'path': 'image/deerUNREL_negSOA.png'},
    {'name': 'image/deerUNREL_negSOA2.png', 'path': 'image/deerUNREL_negSOA2.png'},
    {'name': 'image/vestNEU_negSOA.png', 'path': 'image/vestNEU_negSOA.png'},
    {'name': 'image/vestNEU_negSOA2.png', 'path': 'image/vestNEU_negSOA2.png'},
    {'name': 'image/pistolUNREL_negSOA.png', 'path': 'image/pistolUNREL_negSOA.png'},
    {'name': 'image/pistolUNREL_negSOA2.png', 'path': 'image/pistolUNREL_negSOA2.png'},
    {'name': 'image/vestREL_negSOA.png', 'path': 'image/vestREL_negSOA.png'},
    {'name': 'image/vestREL_negSOA2.png', 'path': 'image/vestREL_negSOA2.png'},
    {'name': 'image/church_NEU.png', 'path': 'image/church_NEU.png'},
    {'name': 'image/church_NEU2.png', 'path': 'image/church_NEU2.png'},
    {'name': 'image/rabbitREL_negSOA.png', 'path': 'image/rabbitREL_negSOA.png'},
    {'name': 'image/rabbitREL_negSOA2.png', 'path': 'image/rabbitREL_negSOA2.png'},
    {'name': 'image/churchID_posSOA.png', 'path': 'image/churchID_posSOA.png'},
    {'name': 'image/churchID_posSOA2.png', 'path': 'image/churchID_posSOA2.png'},
    {'name': 'image/bed_UNREL.png', 'path': 'image/bed_UNREL.png'},
    {'name': 'image/bed_UNREL2.png', 'path': 'image/bed_UNREL2.png'},
    {'name': 'image/desk_NEU.png', 'path': 'image/desk_NEU.png'},
    {'name': 'image/desk_NEU2.png', 'path': 'image/desk_NEU2.png'},
    {'name': 'image/factoryID_negSOA.png', 'path': 'image/factoryID_negSOA.png'},
    {'name': 'image/factoryID_negSOA2.png', 'path': 'image/factoryID_negSOA2.png'},
    {'name': 'image/coatREL_posSOA.png', 'path': 'image/coatREL_posSOA.png'},
    {'name': 'image/coatREL_posSOA2.png', 'path': 'image/coatREL_posSOA2.png'},
    {'name': 'image/factoryID_posSOA.png', 'path': 'image/factoryID_posSOA.png'},
    {'name': 'image/factoryID_posSOA2.png', 'path': 'image/factoryID_posSOA2.png'},
    {'name': 'image/plateREL_negSOA.png', 'path': 'image/plateREL_negSOA.png'},
    {'name': 'image/plateREL_negSOA2.png', 'path': 'image/plateREL_negSOA2.png'},
    {'name': 'image/cannonNEU_posSOA.png', 'path': 'image/cannonNEU_posSOA.png'},
    {'name': 'image/cannonNEU_posSOA2.png', 'path': 'image/cannonNEU_posSOA2.png'},
    {'name': 'image/glassREL_posSOA.png', 'path': 'image/glassREL_posSOA.png'},
    {'name': 'image/glassREL_posSOA2.png', 'path': 'image/glassREL_posSOA2.png'},
    {'name': 'image/trainUNREL_posSOA.png', 'path': 'image/trainUNREL_posSOA.png'},
    {'name': 'image/trainUNREL_posSOA2.png', 'path': 'image/trainUNREL_posSOA2.png'},
    {'name': 'image/sweaterREL_negSOA.png', 'path': 'image/sweaterREL_negSOA.png'},
    {'name': 'image/sweaterREL_negSOA2.png', 'path': 'image/sweaterREL_negSOA2.png'},
    {'name': 'image/cannonREL_negSOA.png', 'path': 'image/cannonREL_negSOA.png'},
    {'name': 'image/cannonREL_negSOA2.png', 'path': 'image/cannonREL_negSOA2.png'},
    {'name': 'image/noseNEU_negSOA.png', 'path': 'image/noseNEU_negSOA.png'},
    {'name': 'image/noseNEU_negSOA2.png', 'path': 'image/noseNEU_negSOA2.png'},
    {'name': 'image/wardrobeID_negSOA.png', 'path': 'image/wardrobeID_negSOA.png'},
    {'name': 'image/wardrobeID_negSOA2.png', 'path': 'image/wardrobeID_negSOA2.png'},
    {'name': 'image/earREL_posSOA.png', 'path': 'image/earREL_posSOA.png'},
    {'name': 'image/earREL_posSOA2.png', 'path': 'image/earREL_posSOA2.png'},
    {'name': 'image/swanNEU_posSOA.png', 'path': 'image/swanNEU_posSOA.png'},
    {'name': 'image/swanNEU_posSOA2.png', 'path': 'image/swanNEU_posSOA2.png'},
    {'name': 'image/jugREL_posSOA.png', 'path': 'image/jugREL_posSOA.png'},
    {'name': 'image/jugREL_posSOA2.png', 'path': 'image/jugREL_posSOA2.png'},
    {'name': 'image/earUNREL_posSOA.png', 'path': 'image/earUNREL_posSOA.png'},
    {'name': 'image/earUNREL_posSOA2.png', 'path': 'image/earUNREL_posSOA2.png'},
    {'name': 'image/swan_ID.png', 'path': 'image/swan_ID.png'},
    {'name': 'image/swan_ID2.png', 'path': 'image/swan_ID2.png'},
    {'name': 'image/glassNEU_negSOA.png', 'path': 'image/glassNEU_negSOA.png'},
    {'name': 'image/glassNEU_negSOA2.png', 'path': 'image/glassNEU_negSOA2.png'},
    {'name': 'image/trainID_negSOA.png', 'path': 'image/trainID_negSOA.png'},
    {'name': 'image/trainID_negSOA2.png', 'path': 'image/trainID_negSOA2.png'},
    {'name': 'image/armUNREL_posSOA.png', 'path': 'image/armUNREL_posSOA.png'},
    {'name': 'image/armUNREL_posSOA2.png', 'path': 'image/armUNREL_posSOA2.png'},
    {'name': 'image/leg_NEU.png', 'path': 'image/leg_NEU.png'},
    {'name': 'image/leg_NEU2.png', 'path': 'image/leg_NEU2.png'},
    {'name': 'image/bikeREL_posSOA.png', 'path': 'image/bikeREL_posSOA.png'},
    {'name': 'image/bikeREL_posSOA2.png', 'path': 'image/bikeREL_posSOA2.png'},
    {'name': 'image/churchID_negSOA.png', 'path': 'image/churchID_negSOA.png'},
    {'name': 'image/churchID_negSOA2.png', 'path': 'image/churchID_negSOA2.png'},
    {'name': 'image/daggerNEU_posSOA.png', 'path': 'image/daggerNEU_posSOA.png'},
    {'name': 'image/daggerNEU_posSOA2.png', 'path': 'image/daggerNEU_posSOA2.png'},
    {'name': 'image/vest_ID.png', 'path': 'image/vest_ID.png'},
    {'name': 'image/vest_ID2.png', 'path': 'image/vest_ID2.png'},
    {'name': 'image/car_ID.png', 'path': 'image/car_ID.png'},
    {'name': 'image/car_ID2.png', 'path': 'image/car_ID2.png'},
    {'name': 'image/pistol_UNREL.png', 'path': 'image/pistol_UNREL.png'},
    {'name': 'image/pistol_UNREL2.png', 'path': 'image/pistol_UNREL2.png'},
    {'name': 'image/cupUNREL_posSOA.png', 'path': 'image/cupUNREL_posSOA.png'},
    {'name': 'image/cupUNREL_posSOA2.png', 'path': 'image/cupUNREL_posSOA2.png'},
    {'name': 'image/car_UNREL.png', 'path': 'image/car_UNREL.png'},
    {'name': 'image/car_UNREL2.png', 'path': 'image/car_UNREL2.png'},
    {'name': 'image/factoryNEU_negSOA.png', 'path': 'image/factoryNEU_negSOA.png'},
    {'name': 'image/factoryNEU_negSOA2.png', 'path': 'image/factoryNEU_negSOA2.png'},
    {'name': 'image/glass_ID.png', 'path': 'image/glass_ID.png'},
    {'name': 'image/glass_ID2.png', 'path': 'image/glass_ID2.png'},
    {'name': 'image/bedID_negSOA.png', 'path': 'image/bedID_negSOA.png'},
    {'name': 'image/bedID_negSOA2.png', 'path': 'image/bedID_negSOA2.png'},
    {'name': 'image/carUNREL_negSOA.png', 'path': 'image/carUNREL_negSOA.png'},
    {'name': 'image/carUNREL_negSOA2.png', 'path': 'image/carUNREL_negSOA2.png'},
    {'name': 'image/tortoiseNEU_negSOA.png', 'path': 'image/tortoiseNEU_negSOA.png'},
    {'name': 'image/tortoiseNEU_negSOA2.png', 'path': 'image/tortoiseNEU_negSOA2.png'},
    {'name': 'image/car_REL.png', 'path': 'image/car_REL.png'},
    {'name': 'image/car_REL2.png', 'path': 'image/car_REL2.png'},
    {'name': 'image/nose_REL.png', 'path': 'image/nose_REL.png'},
    {'name': 'image/nose_REL2.png', 'path': 'image/nose_REL2.png'},
    {'name': 'image/legNEU_posSOA.png', 'path': 'image/legNEU_posSOA.png'},
    {'name': 'image/legNEU_posSOA2.png', 'path': 'image/legNEU_posSOA2.png'},
    {'name': 'image/bikeID_posSOA.png', 'path': 'image/bikeID_posSOA.png'},
    {'name': 'image/bikeID_posSOA2.png', 'path': 'image/bikeID_posSOA2.png'},
    {'name': 'image/planeID_posSOA.png', 'path': 'image/planeID_posSOA.png'},
    {'name': 'image/planeID_posSOA2.png', 'path': 'image/planeID_posSOA2.png'},
    {'name': 'image/cup_NEU.png', 'path': 'image/cup_NEU.png'},
    {'name': 'image/cup_NEU2.png', 'path': 'image/cup_NEU2.png'},
    {'name': 'image/glass_REL.png', 'path': 'image/glass_REL.png'},
    {'name': 'image/glass_REL2.png', 'path': 'image/glass_REL2.png'},
    {'name': 'image/deer_REL.png', 'path': 'image/deer_REL.png'},
    {'name': 'image/deer_REL2.png', 'path': 'image/deer_REL2.png'},
    {'name': 'image/plateNEU_posSOA.png', 'path': 'image/plateNEU_posSOA.png'},
    {'name': 'image/plateNEU_posSOA2.png', 'path': 'image/plateNEU_posSOA2.png'},
    {'name': 'image/legREL_posSOA.png', 'path': 'image/legREL_posSOA.png'},
    {'name': 'image/legREL_posSOA2.png', 'path': 'image/legREL_posSOA2.png'},
    {'name': 'image/daggerREL_posSOA.png', 'path': 'image/daggerREL_posSOA.png'},
    {'name': 'image/daggerREL_posSOA2.png', 'path': 'image/daggerREL_posSOA2.png'},
    {'name': 'image/jugNEU_posSOA.png', 'path': 'image/jugNEU_posSOA.png'},
    {'name': 'image/jugNEU_posSOA2.png', 'path': 'image/jugNEU_posSOA2.png'},
    {'name': 'image/churchREL_negSOA.png', 'path': 'image/churchREL_negSOA.png'},
    {'name': 'image/churchREL_negSOA2.png', 'path': 'image/churchREL_negSOA2.png'},
    {'name': 'image/skirt_ID.png', 'path': 'image/skirt_ID.png'},
    {'name': 'image/skirt_ID2.png', 'path': 'image/skirt_ID2.png'},
    {'name': 'image/bike_NEU.png', 'path': 'image/bike_NEU.png'},
    {'name': 'image/bike_NEU2.png', 'path': 'image/bike_NEU2.png'},
    {'name': 'image/table_UNREL.png', 'path': 'image/table_UNREL.png'},
    {'name': 'image/table_UNREL2.png', 'path': 'image/table_UNREL2.png'},
    {'name': 'image/deskUNREL_negSOA.png', 'path': 'image/deskUNREL_negSOA.png'},
    {'name': 'image/deskUNREL_negSOA2.png', 'path': 'image/deskUNREL_negSOA2.png'},
    {'name': 'image/skirtNEU_negSOA.png', 'path': 'image/skirtNEU_negSOA.png'},
    {'name': 'image/skirtNEU_negSOA2.png', 'path': 'image/skirtNEU_negSOA2.png'},
    {'name': 'image/church_UNREL.png', 'path': 'image/church_UNREL.png'},
    {'name': 'image/church_UNREL2.png', 'path': 'image/church_UNREL2.png'},
    {'name': 'image/skirtID_posSOA.png', 'path': 'image/skirtID_posSOA.png'},
    {'name': 'image/skirtID_posSOA2.png', 'path': 'image/skirtID_posSOA2.png'},
    {'name': 'image/dagger_ID.png', 'path': 'image/dagger_ID.png'},
    {'name': 'image/dagger_ID2.png', 'path': 'image/dagger_ID2.png'},
    {'name': 'exp_items_s2.csv', 'path': 'exp_items_s2.csv'},
    {'name': 'image/carID_posSOA.png', 'path': 'image/carID_posSOA.png'},
    {'name': 'image/carID_posSOA2.png', 'path': 'image/carID_posSOA2.png'},
    {'name': 'image/jugUNREL_negSOA.png', 'path': 'image/jugUNREL_negSOA.png'},
    {'name': 'image/jugUNREL_negSOA2.png', 'path': 'image/jugUNREL_negSOA2.png'},
    {'name': 'image/cannonNEU_negSOA.png', 'path': 'image/cannonNEU_negSOA.png'},
    {'name': 'image/cannonNEU_negSOA2.png', 'path': 'image/cannonNEU_negSOA2.png'},
    {'name': 'image/bikeUNREL_posSOA.png', 'path': 'image/bikeUNREL_posSOA.png'},
    {'name': 'image/bikeUNREL_posSOA2.png', 'path': 'image/bikeUNREL_posSOA2.png'},
    {'name': 'image/planeUNREL_posSOA.png', 'path': 'image/planeUNREL_posSOA.png'},
    {'name': 'image/planeUNREL_posSOA2.png', 'path': 'image/planeUNREL_posSOA2.png'},
    {'name': 'image/jug_NEU.png', 'path': 'image/jug_NEU.png'},
    {'name': 'image/jug_NEU2.png', 'path': 'image/jug_NEU2.png'},
    {'name': 'image/bedUNREL_negSOA.png', 'path': 'image/bedUNREL_negSOA.png'},
    {'name': 'image/bedUNREL_negSOA2.png', 'path': 'image/bedUNREL_negSOA2.png'},
    {'name': 'image/deer_UNREL.png', 'path': 'image/deer_UNREL.png'},
    {'name': 'image/deer_UNREL2.png', 'path': 'image/deer_UNREL2.png'},
    {'name': 'image/plane_UNREL.png', 'path': 'image/plane_UNREL.png'},
    {'name': 'image/plane_UNREL2.png', 'path': 'image/plane_UNREL2.png'},
    {'name': 'image/cupNEU_posSOA.png', 'path': 'image/cupNEU_posSOA.png'},
    {'name': 'image/cupNEU_posSOA2.png', 'path': 'image/cupNEU_posSOA2.png'},
    {'name': 'image/ear_ID.png', 'path': 'image/ear_ID.png'},
    {'name': 'image/ear_ID2.png', 'path': 'image/ear_ID2.png'},
    {'name': 'image/vestUNREL_negSOA.png', 'path': 'image/vestUNREL_negSOA.png'},
    {'name': 'image/vestUNREL_negSOA2.png', 'path': 'image/vestUNREL_negSOA2.png'},
    {'name': 'image/tortoiseUNREL_negSOA.png', 'path': 'image/tortoiseUNREL_negSOA.png'},
    {'name': 'image/tortoiseUNREL_negSOA2.png', 'path': 'image/tortoiseUNREL_negSOA2.png'},
    {'name': 'image/plateNEU_negSOA.png', 'path': 'image/plateNEU_negSOA.png'},
    {'name': 'image/plateNEU_negSOA2.png', 'path': 'image/plateNEU_negSOA2.png'},
    {'name': 'image/bed_REL.png', 'path': 'image/bed_REL.png'},
    {'name': 'image/bed_REL2.png', 'path': 'image/bed_REL2.png'},
    {'name': 'image/jugREL_negSOA.png', 'path': 'image/jugREL_negSOA.png'},
    {'name': 'image/jugREL_negSOA2.png', 'path': 'image/jugREL_negSOA2.png'},
    {'name': 'image/windmillUNREL_negSOA.png', 'path': 'image/windmillUNREL_negSOA.png'},
    {'name': 'image/windmillUNREL_negSOA2.png', 'path': 'image/windmillUNREL_negSOA2.png'},
    {'name': 'image/vestNEU_posSOA.png', 'path': 'image/vestNEU_posSOA.png'},
    {'name': 'image/vestNEU_posSOA2.png', 'path': 'image/vestNEU_posSOA2.png'},
    {'name': 'image/bike_ID.png', 'path': 'image/bike_ID.png'},
    {'name': 'image/bike_ID2.png', 'path': 'image/bike_ID2.png'},
    {'name': 'image/castle_ID.png', 'path': 'image/castle_ID.png'},
    {'name': 'image/castle_ID2.png', 'path': 'image/castle_ID2.png'},
    {'name': 'image/rabbit_NEU.png', 'path': 'image/rabbit_NEU.png'},
    {'name': 'image/rabbit_NEU2.png', 'path': 'image/rabbit_NEU2.png'},
    {'name': 'image/deerREL_posSOA.png', 'path': 'image/deerREL_posSOA.png'},
    {'name': 'image/deerREL_posSOA2.png', 'path': 'image/deerREL_posSOA2.png'},
    {'name': 'image/glass_NEU.png', 'path': 'image/glass_NEU.png'},
    {'name': 'image/glass_NEU2.png', 'path': 'image/glass_NEU2.png'},
    {'name': 'image/bedUNREL_posSOA.png', 'path': 'image/bedUNREL_posSOA.png'},
    {'name': 'image/bedUNREL_posSOA2.png', 'path': 'image/bedUNREL_posSOA2.png'},
    {'name': 'image/wardrobe_NEU.png', 'path': 'image/wardrobe_NEU.png'},
    {'name': 'image/wardrobe_NEU2.png', 'path': 'image/wardrobe_NEU2.png'},
    {'name': 'image/vestID_posSOA.png', 'path': 'image/vestID_posSOA.png'},
    {'name': 'image/vestID_posSOA2.png', 'path': 'image/vestID_posSOA2.png'},
    {'name': 'image/glassREL_negSOA.png', 'path': 'image/glassREL_negSOA.png'},
    {'name': 'image/glassREL_negSOA2.png', 'path': 'image/glassREL_negSOA2.png'},
    {'name': 'image/tortoiseNEU_posSOA.png', 'path': 'image/tortoiseNEU_posSOA.png'},
    {'name': 'image/tortoiseNEU_posSOA2.png', 'path': 'image/tortoiseNEU_posSOA2.png'},
    {'name': 'image/arm_UNREL.png', 'path': 'image/arm_UNREL.png'},
    {'name': 'image/arm_UNREL2.png', 'path': 'image/arm_UNREL2.png'},
    {'name': 'image/cupREL_posSOA.png', 'path': 'image/cupREL_posSOA.png'},
    {'name': 'image/cupREL_posSOA2.png', 'path': 'image/cupREL_posSOA2.png'},
    {'name': 'image/deerNEU_posSOA.png', 'path': 'image/deerNEU_posSOA.png'},
    {'name': 'image/deerNEU_posSOA2.png', 'path': 'image/deerNEU_posSOA2.png'},
    {'name': 'image/cupUNREL_negSOA.png', 'path': 'image/cupUNREL_negSOA.png'},
    {'name': 'image/cupUNREL_negSOA2.png', 'path': 'image/cupUNREL_negSOA2.png'},
    {'name': 'image/rabbitNEU_negSOA.png', 'path': 'image/rabbitNEU_negSOA.png'},
    {'name': 'image/rabbitNEU_negSOA2.png', 'path': 'image/rabbitNEU_negSOA2.png'},
    {'name': 'image/swanID_posSOA.png', 'path': 'image/swanID_posSOA.png'},
    {'name': 'image/swanID_posSOA2.png', 'path': 'image/swanID_posSOA2.png'},
    {'name': 'image/leg_ID.png', 'path': 'image/leg_ID.png'},
    {'name': 'image/leg_ID2.png', 'path': 'image/leg_ID2.png'},
    {'name': 'image/factoryUNREL_posSOA.png', 'path': 'image/factoryUNREL_posSOA.png'},
    {'name': 'image/factoryUNREL_posSOA2.png', 'path': 'image/factoryUNREL_posSOA2.png'},
    {'name': 'image/skirtNEU_posSOA.png', 'path': 'image/skirtNEU_posSOA.png'},
    {'name': 'image/skirtNEU_posSOA2.png', 'path': 'image/skirtNEU_posSOA2.png'},
    {'name': 'image/plate_REL.png', 'path': 'image/plate_REL.png'},
    {'name': 'image/plate_REL2.png', 'path': 'image/plate_REL2.png'},
    {'name': 'image/daggerUNREL_posSOA.png', 'path': 'image/daggerUNREL_posSOA.png'},
    {'name': 'image/daggerUNREL_posSOA2.png', 'path': 'image/daggerUNREL_posSOA2.png'},
    {'name': 'image/cannon_NEU.png', 'path': 'image/cannon_NEU.png'},
    {'name': 'image/cannon_NEU2.png', 'path': 'image/cannon_NEU2.png'},
    {'name': 'image/vestREL_posSOA.png', 'path': 'image/vestREL_posSOA.png'},
    {'name': 'image/vestREL_posSOA2.png', 'path': 'image/vestREL_posSOA2.png'},
    {'name': 'image/armID_posSOA.png', 'path': 'image/armID_posSOA.png'},
    {'name': 'image/armID_posSOA2.png', 'path': 'image/armID_posSOA2.png'},
    {'name': 'image/glassNEU_posSOA.png', 'path': 'image/glassNEU_posSOA.png'},
    {'name': 'image/glassNEU_posSOA2.png', 'path': 'image/glassNEU_posSOA2.png'},
    {'name': 'image/swanUNREL_negSOA.png', 'path': 'image/swanUNREL_negSOA.png'},
    {'name': 'image/swanUNREL_negSOA2.png', 'path': 'image/swanUNREL_negSOA2.png'},
    {'name': 'image/rabbitUNREL_posSOA.png', 'path': 'image/rabbitUNREL_posSOA.png'},
    {'name': 'image/rabbitUNREL_posSOA2.png', 'path': 'image/rabbitUNREL_posSOA2.png'},
    {'name': 'image/tortoiseREL_posSOA.png', 'path': 'image/tortoiseREL_posSOA.png'},
    {'name': 'image/tortoiseREL_posSOA2.png', 'path': 'image/tortoiseREL_posSOA2.png'},
    {'name': 'image/armNEU_posSOA.png', 'path': 'image/armNEU_posSOA.png'},
    {'name': 'image/armNEU_posSOA2.png', 'path': 'image/armNEU_posSOA2.png'},
    {'name': 'image/deskID_negSOA.png', 'path': 'image/deskID_negSOA.png'},
    {'name': 'image/deskID_negSOA2.png', 'path': 'image/deskID_negSOA2.png'},
    {'name': 'image/table_NEU.png', 'path': 'image/table_NEU.png'},
    {'name': 'image/table_NEU2.png', 'path': 'image/table_NEU2.png'},
    {'name': 'image/armUNREL_negSOA.png', 'path': 'image/armUNREL_negSOA.png'},
    {'name': 'image/armUNREL_negSOA2.png', 'path': 'image/armUNREL_negSOA2.png'},
    {'name': 'image/plane_REL.png', 'path': 'image/plane_REL.png'},
    {'name': 'image/plane_REL2.png', 'path': 'image/plane_REL2.png'},
    {'name': 'image/tableNEU_negSOA.png', 'path': 'image/tableNEU_negSOA.png'},
    {'name': 'image/tableNEU_negSOA2.png', 'path': 'image/tableNEU_negSOA2.png'},
    {'name': 'image/armREL_negSOA.png', 'path': 'image/armREL_negSOA.png'},
    {'name': 'image/armREL_negSOA2.png', 'path': 'image/armREL_negSOA2.png'},
    {'name': 'image/swan_UNREL.png', 'path': 'image/swan_UNREL.png'},
    {'name': 'image/swan_UNREL2.png', 'path': 'image/swan_UNREL2.png'},
    {'name': 'image/sweaterNEU_posSOA.png', 'path': 'image/sweaterNEU_posSOA.png'},
    {'name': 'image/sweaterNEU_posSOA2.png', 'path': 'image/sweaterNEU_posSOA2.png'},
    {'name': 'image/noseID_posSOA.png', 'path': 'image/noseID_posSOA.png'},
    {'name': 'image/noseID_posSOA2.png', 'path': 'image/noseID_posSOA2.png'},
    {'name': 'image/legREL_negSOA.png', 'path': 'image/legREL_negSOA.png'},
    {'name': 'image/legREL_negSOA2.png', 'path': 'image/legREL_negSOA2.png'},
    {'name': 'image/legNEU_negSOA.png', 'path': 'image/legNEU_negSOA.png'},
    {'name': 'image/legNEU_negSOA2.png', 'path': 'image/legNEU_negSOA2.png'},
    {'name': 'image/windmillREL_posSOA.png', 'path': 'image/windmillREL_posSOA.png'},
    {'name': 'image/windmillREL_posSOA2.png', 'path': 'image/windmillREL_posSOA2.png'},
    {'name': 'image/swanUNREL_posSOA.png', 'path': 'image/swanUNREL_posSOA.png'},
    {'name': 'image/swanUNREL_posSOA2.png', 'path': 'image/swanUNREL_posSOA2.png'},
    {'name': 'image/plate_ID.png', 'path': 'image/plate_ID.png'},
    {'name': 'image/plate_ID2.png', 'path': 'image/plate_ID2.png'},
    {'name': 'image/swordNEU_posSOA.png', 'path': 'image/swordNEU_posSOA.png'},
    {'name': 'image/swordNEU_posSOA2.png', 'path': 'image/swordNEU_posSOA2.png'},
    {'name': 'image/carID_negSOA.png', 'path': 'image/carID_negSOA.png'},
    {'name': 'image/carID_negSOA2.png', 'path': 'image/carID_negSOA2.png'},
    {'name': 'image/arm_REL.png', 'path': 'image/arm_REL.png'},
    {'name': 'image/arm_REL2.png', 'path': 'image/arm_REL2.png'},
    {'name': 'image/desk_ID.png', 'path': 'image/desk_ID.png'},
    {'name': 'image/desk_ID2.png', 'path': 'image/desk_ID2.png'},
    {'name': 'image/trainID_posSOA.png', 'path': 'image/trainID_posSOA.png'},
    {'name': 'image/trainID_posSOA2.png', 'path': 'image/trainID_posSOA2.png'},
    {'name': 'image/pistolID_negSOA.png', 'path': 'image/pistolID_negSOA.png'},
    {'name': 'image/pistolID_negSOA2.png', 'path': 'image/pistolID_negSOA2.png'},
    {'name': 'image/deskNEU_negSOA.png', 'path': 'image/deskNEU_negSOA.png'},
    {'name': 'image/deskNEU_negSOA2.png', 'path': 'image/deskNEU_negSOA2.png'},
    {'name': 'image/churchUNREL_negSOA.png', 'path': 'image/churchUNREL_negSOA.png'},
    {'name': 'image/churchUNREL_negSOA2.png', 'path': 'image/churchUNREL_negSOA2.png'},
    {'name': 'image/earREL_negSOA.png', 'path': 'image/earREL_negSOA.png'},
    {'name': 'image/earREL_negSOA2.png', 'path': 'image/earREL_negSOA2.png'},
    {'name': 'image/sweaterID_posSOA.png', 'path': 'image/sweaterID_posSOA.png'},
    {'name': 'image/sweaterID_posSOA2.png', 'path': 'image/sweaterID_posSOA2.png'},
    {'name': 'image/castle_UNREL.png', 'path': 'image/castle_UNREL.png'},
    {'name': 'image/castle_UNREL2.png', 'path': 'image/castle_UNREL2.png'},
    {'name': 'image/sweaterREL_posSOA.png', 'path': 'image/sweaterREL_posSOA.png'},
    {'name': 'image/sweaterREL_posSOA2.png', 'path': 'image/sweaterREL_posSOA2.png'},
    {'name': 'image/trainREL_negSOA.png', 'path': 'image/trainREL_negSOA.png'},
    {'name': 'image/trainREL_negSOA2.png', 'path': 'image/trainREL_negSOA2.png'},
    {'name': 'image/cannonID_negSOA.png', 'path': 'image/cannonID_negSOA.png'},
    {'name': 'image/cannonID_negSOA2.png', 'path': 'image/cannonID_negSOA2.png'},
    {'name': 'image/arm_NEU.png', 'path': 'image/arm_NEU.png'},
    {'name': 'image/arm_NEU2.png', 'path': 'image/arm_NEU2.png'},
    {'name': 'image/windmill_REL.png', 'path': 'image/windmill_REL.png'},
    {'name': 'image/windmill_REL2.png', 'path': 'image/windmill_REL2.png'},
    {'name': 'image/rabbitID_posSOA.png', 'path': 'image/rabbitID_posSOA.png'},
    {'name': 'image/rabbitID_posSOA2.png', 'path': 'image/rabbitID_posSOA2.png'},
    {'name': 'image/plateID_negSOA.png', 'path': 'image/plateID_negSOA.png'},
    {'name': 'image/plateID_negSOA2.png', 'path': 'image/plateID_negSOA2.png'},
    {'name': 'image/sweaterID_negSOA.png', 'path': 'image/sweaterID_negSOA.png'},
    {'name': 'image/sweaterID_negSOA2.png', 'path': 'image/sweaterID_negSOA2.png'},
    {'name': 'image/coat_NEU.png', 'path': 'image/coat_NEU.png'},
    {'name': 'image/coat_NEU2.png', 'path': 'image/coat_NEU2.png'},
    {'name': 'image/cup_UNREL.png', 'path': 'image/cup_UNREL.png'},
    {'name': 'image/cup_UNREL2.png', 'path': 'image/cup_UNREL2.png'},
    {'name': 'image/plateUNREL_negSOA.png', 'path': 'image/plateUNREL_negSOA.png'},
    {'name': 'image/plateUNREL_negSOA2.png', 'path': 'image/plateUNREL_negSOA2.png'},
    {'name': 'image/skirt_REL.png', 'path': 'image/skirt_REL.png'},
    {'name': 'image/skirt_REL2.png', 'path': 'image/skirt_REL2.png'},
    {'name': 'image/rabbit_REL.png', 'path': 'image/rabbit_REL.png'},
    {'name': 'image/rabbit_REL2.png', 'path': 'image/rabbit_REL2.png'},
    {'name': 'image/swanID_negSOA.png', 'path': 'image/swanID_negSOA.png'},
    {'name': 'image/swanID_negSOA2.png', 'path': 'image/swanID_negSOA2.png'},
    {'name': 'image/cannonUNREL_posSOA.png', 'path': 'image/cannonUNREL_posSOA.png'},
    {'name': 'image/cannonUNREL_posSOA2.png', 'path': 'image/cannonUNREL_posSOA2.png'},
    {'name': 'image/bikeREL_negSOA.png', 'path': 'image/bikeREL_negSOA.png'},
    {'name': 'image/bikeREL_negSOA2.png', 'path': 'image/bikeREL_negSOA2.png'},
    {'name': 'image/bikeID_negSOA.png', 'path': 'image/bikeID_negSOA.png'},
    {'name': 'image/bikeID_negSOA2.png', 'path': 'image/bikeID_negSOA2.png'},
    {'name': 'image/bedID_posSOA.png', 'path': 'image/bedID_posSOA.png'},
    {'name': 'image/bedID_posSOA2.png', 'path': 'image/bedID_posSOA2.png'},
    {'name': 'image/castleREL_posSOA.png', 'path': 'image/castleREL_posSOA.png'},
    {'name': 'image/castleREL_posSOA2.png', 'path': 'image/castleREL_posSOA2.png'},
    {'name': 'image/jugID_posSOA.png', 'path': 'image/jugID_posSOA.png'},
    {'name': 'image/jugID_posSOA2.png', 'path': 'image/jugID_posSOA2.png'},
    {'name': 'image/wardrobe_REL.png', 'path': 'image/wardrobe_REL.png'},
    {'name': 'image/wardrobe_REL2.png', 'path': 'image/wardrobe_REL2.png'},
    {'name': 'image/deerREL_negSOA.png', 'path': 'image/deerREL_negSOA.png'},
    {'name': 'image/deerREL_negSOA2.png', 'path': 'image/deerREL_negSOA2.png'},
    {'name': 'image/sword_UNREL.png', 'path': 'image/sword_UNREL.png'},
    {'name': 'image/sword_UNREL2.png', 'path': 'image/sword_UNREL2.png'},
    {'name': 'image/noseNEU_posSOA.png', 'path': 'image/noseNEU_posSOA.png'},
    {'name': 'image/noseNEU_posSOA2.png', 'path': 'image/noseNEU_posSOA2.png'},
    {'name': 'exp_items_s3.csv', 'path': 'exp_items_s3.csv'},
    {'name': 'image/wardrobeID_posSOA.png', 'path': 'image/wardrobeID_posSOA.png'},
    {'name': 'image/wardrobeID_posSOA2.png', 'path': 'image/wardrobeID_posSOA2.png'},
    {'name': 'image/coatNEU_negSOA.png', 'path': 'image/coatNEU_negSOA.png'},
    {'name': 'image/coatNEU_negSOA2.png', 'path': 'image/coatNEU_negSOA2.png'},
    {'name': 'image/cannonREL_posSOA.png', 'path': 'image/cannonREL_posSOA.png'},
    {'name': 'image/cannonREL_posSOA2.png', 'path': 'image/cannonREL_posSOA2.png'},
    {'name': 'image/rabbitREL_posSOA.png', 'path': 'image/rabbitREL_posSOA.png'},
    {'name': 'image/rabbitREL_posSOA2.png', 'path': 'image/rabbitREL_posSOA2.png'},
    {'name': 'image/cupNEU_negSOA.png', 'path': 'image/cupNEU_negSOA.png'},
    {'name': 'image/cupNEU_negSOA2.png', 'path': 'image/cupNEU_negSOA2.png'},
    {'name': 'image/arm_ID.png', 'path': 'image/arm_ID.png'},
    {'name': 'image/arm_ID2.png', 'path': 'image/arm_ID2.png'},
    {'name': 'image/castleREL_negSOA.png', 'path': 'image/castleREL_negSOA.png'},
    {'name': 'image/castleREL_negSOA2.png', 'path': 'image/castleREL_negSOA2.png'},
    {'name': 'image/carNEU_negSOA.png', 'path': 'image/carNEU_negSOA.png'},
    {'name': 'image/carNEU_negSOA2.png', 'path': 'image/carNEU_negSOA2.png'},
    {'name': 'image/rabbitUNREL_negSOA.png', 'path': 'image/rabbitUNREL_negSOA.png'},
    {'name': 'image/rabbitUNREL_negSOA2.png', 'path': 'image/rabbitUNREL_negSOA2.png'},
    {'name': 'image/cannon_REL.png', 'path': 'image/cannon_REL.png'},
    {'name': 'image/cannon_REL2.png', 'path': 'image/cannon_REL2.png'},
    {'name': 'image/carNEU_posSOA.png', 'path': 'image/carNEU_posSOA.png'},
    {'name': 'image/carNEU_posSOA2.png', 'path': 'image/carNEU_posSOA2.png'},
    {'name': 'image/train_UNREL.png', 'path': 'image/train_UNREL.png'},
    {'name': 'image/train_UNREL2.png', 'path': 'image/train_UNREL2.png'},
    {'name': 'image/glassUNREL_negSOA.png', 'path': 'image/glassUNREL_negSOA.png'},
    {'name': 'image/glassUNREL_negSOA2.png', 'path': 'image/glassUNREL_negSOA2.png'},
    {'name': 'image/tableREL_negSOA.png', 'path': 'image/tableREL_negSOA.png'},
    {'name': 'image/tableREL_negSOA2.png', 'path': 'image/tableREL_negSOA2.png'},
    {'name': 'image/daggerUNREL_negSOA.png', 'path': 'image/daggerUNREL_negSOA.png'},
    {'name': 'image/daggerUNREL_negSOA2.png', 'path': 'image/daggerUNREL_negSOA2.png'},
    {'name': 'image/deskREL_posSOA.png', 'path': 'image/deskREL_posSOA.png'},
    {'name': 'image/deskREL_posSOA2.png', 'path': 'image/deskREL_posSOA2.png'},
    {'name': 'image/coatID_negSOA.png', 'path': 'image/coatID_negSOA.png'},
    {'name': 'image/coatID_negSOA2.png', 'path': 'image/coatID_negSOA2.png'},
    {'name': 'image/castle_NEU.png', 'path': 'image/castle_NEU.png'},
    {'name': 'image/castle_NEU2.png', 'path': 'image/castle_NEU2.png'},
    {'name': 'image/cupID_negSOA.png', 'path': 'image/cupID_negSOA.png'},
    {'name': 'image/cupID_negSOA2.png', 'path': 'image/cupID_negSOA2.png'},
    {'name': 'image/pistolUNREL_posSOA.png', 'path': 'image/pistolUNREL_posSOA.png'},
    {'name': 'image/pistolUNREL_posSOA2.png', 'path': 'image/pistolUNREL_posSOA2.png'},
    {'name': 'image/coat_UNREL.png', 'path': 'image/coat_UNREL.png'},
    {'name': 'image/coat_UNREL2.png', 'path': 'image/coat_UNREL2.png'},
    {'name': 'image/armID_negSOA.png', 'path': 'image/armID_negSOA.png'},
    {'name': 'image/armID_negSOA2.png', 'path': 'image/armID_negSOA2.png'},
    {'name': 'image/swanREL_posSOA.png', 'path': 'image/swanREL_posSOA.png'},
    {'name': 'image/swanREL_posSOA2.png', 'path': 'image/swanREL_posSOA2.png'},
    {'name': 'image/plate_NEU.png', 'path': 'image/plate_NEU.png'},
    {'name': 'image/plate_NEU2.png', 'path': 'image/plate_NEU2.png'},
    {'name': 'image/leg_REL.png', 'path': 'image/leg_REL.png'},
    {'name': 'image/leg_REL2.png', 'path': 'image/leg_REL2.png'},
    {'name': 'image/daggerID_negSOA.png', 'path': 'image/daggerID_negSOA.png'},
    {'name': 'image/daggerID_negSOA2.png', 'path': 'image/daggerID_negSOA2.png'},
    {'name': 'image/car_NEU.png', 'path': 'image/car_NEU.png'},
    {'name': 'image/car_NEU2.png', 'path': 'image/car_NEU2.png'},
    {'name': 'image/church_ID.png', 'path': 'image/church_ID.png'},
    {'name': 'image/church_ID2.png', 'path': 'image/church_ID2.png'},
    {'name': 'image/skirtREL_posSOA.png', 'path': 'image/skirtREL_posSOA.png'},
    {'name': 'image/skirtREL_posSOA2.png', 'path': 'image/skirtREL_posSOA2.png'},
    {'name': 'image/plateREL_posSOA.png', 'path': 'image/plateREL_posSOA.png'},
    {'name': 'image/plateREL_posSOA2.png', 'path': 'image/plateREL_posSOA2.png'},
    {'name': 'image/windmill_NEU.png', 'path': 'image/windmill_NEU.png'},
    {'name': 'image/windmill_NEU2.png', 'path': 'image/windmill_NEU2.png'},
    {'name': 'image/coat_ID.png', 'path': 'image/coat_ID.png'},
    {'name': 'image/coat_ID2.png', 'path': 'image/coat_ID2.png'},
    {'name': 'image/dagger_UNREL.png', 'path': 'image/dagger_UNREL.png'},
    {'name': 'image/dagger_UNREL2.png', 'path': 'image/dagger_UNREL2.png'},
    {'name': 'image/rabbitNEU_posSOA.png', 'path': 'image/rabbitNEU_posSOA.png'},
    {'name': 'image/rabbitNEU_posSOA2.png', 'path': 'image/rabbitNEU_posSOA2.png'},
    {'name': 'image/carUNREL_posSOA.png', 'path': 'image/carUNREL_posSOA.png'},
    {'name': 'image/carUNREL_posSOA2.png', 'path': 'image/carUNREL_posSOA2.png'},
    {'name': 'image/carREL_posSOA.png', 'path': 'image/carREL_posSOA.png'},
    {'name': 'image/carREL_posSOA2.png', 'path': 'image/carREL_posSOA2.png'},
    {'name': 'image/earID_posSOA.png', 'path': 'image/earID_posSOA.png'},
    {'name': 'image/earID_posSOA2.png', 'path': 'image/earID_posSOA2.png'},
    {'name': 'image/swan_NEU.png', 'path': 'image/swan_NEU.png'},
    {'name': 'image/swan_NEU2.png', 'path': 'image/swan_NEU2.png'},
    {'name': 'image/tableUNREL_negSOA.png', 'path': 'image/tableUNREL_negSOA.png'},
    {'name': 'image/tableUNREL_negSOA2.png', 'path': 'image/tableUNREL_negSOA2.png'},
    {'name': 'image/daggerID_posSOA.png', 'path': 'image/daggerID_posSOA.png'},
    {'name': 'image/daggerID_posSOA2.png', 'path': 'image/daggerID_posSOA2.png'},
    {'name': 'image/bikeNEU_negSOA.png', 'path': 'image/bikeNEU_negSOA.png'},
    {'name': 'image/bikeNEU_negSOA2.png', 'path': 'image/bikeNEU_negSOA2.png'},
    {'name': 'image/coatUNREL_negSOA.png', 'path': 'image/coatUNREL_negSOA.png'},
    {'name': 'image/coatUNREL_negSOA2.png', 'path': 'image/coatUNREL_negSOA2.png'},
    {'name': 'image/pistol_ID.png', 'path': 'image/pistol_ID.png'},
    {'name': 'image/pistol_ID2.png', 'path': 'image/pistol_ID2.png'},
    {'name': 'image/sweater_NEU.png', 'path': 'image/sweater_NEU.png'},
    {'name': 'image/sweater_NEU2.png', 'path': 'image/sweater_NEU2.png'},
    {'name': 'image/jug_ID.png', 'path': 'image/jug_ID.png'},
    {'name': 'image/jug_ID2.png', 'path': 'image/jug_ID2.png'},
    {'name': 'image/vest_NEU.png', 'path': 'image/vest_NEU.png'},
    {'name': 'image/vest_NEU2.png', 'path': 'image/vest_NEU2.png'},
    {'name': 'image/sweater_REL.png', 'path': 'image/sweater_REL.png'},
    {'name': 'image/sweater_REL2.png', 'path': 'image/sweater_REL2.png'},
    {'name': 'image/trainREL_posSOA.png', 'path': 'image/trainREL_posSOA.png'},
    {'name': 'image/trainREL_posSOA2.png', 'path': 'image/trainREL_posSOA2.png'},
    {'name': 'image/vest_REL.png', 'path': 'image/vest_REL.png'},
    {'name': 'image/vest_REL2.png', 'path': 'image/vest_REL2.png'},
    {'name': 'image/wardrobeUNREL_posSOA.png', 'path': 'image/wardrobeUNREL_posSOA.png'},
    {'name': 'image/wardrobeUNREL_posSOA2.png', 'path': 'image/wardrobeUNREL_posSOA2.png'},
    {'name': 'image/sword_NEU.png', 'path': 'image/sword_NEU.png'},
    {'name': 'image/sword_NEU2.png', 'path': 'image/sword_NEU2.png'},
    {'name': 'image/windmill_ID.png', 'path': 'image/windmill_ID.png'},
    {'name': 'image/windmill_ID2.png', 'path': 'image/windmill_ID2.png'},
    {'name': 'image/train_REL.png', 'path': 'image/train_REL.png'},
    {'name': 'image/train_REL2.png', 'path': 'image/train_REL2.png'},
    {'name': 'image/skirtREL_negSOA.png', 'path': 'image/skirtREL_negSOA.png'},
    {'name': 'image/skirtREL_negSOA2.png', 'path': 'image/skirtREL_negSOA2.png'},
    {'name': 'image/sweaterUNREL_negSOA.png', 'path': 'image/sweaterUNREL_negSOA.png'},
    {'name': 'image/sweaterUNREL_negSOA2.png', 'path': 'image/sweaterUNREL_negSOA2.png'},
    {'name': 'image/deerNEU_negSOA.png', 'path': 'image/deerNEU_negSOA.png'},
    {'name': 'image/deerNEU_negSOA2.png', 'path': 'image/deerNEU_negSOA2.png'},
    {'name': 'image/swordUNREL_posSOA.png', 'path': 'image/swordUNREL_posSOA.png'},
    {'name': 'image/swordUNREL_posSOA2.png', 'path': 'image/swordUNREL_posSOA2.png'},
    {'name': 'image/plate_UNREL.png', 'path': 'image/plate_UNREL.png'},
    {'name': 'image/plate_UNREL2.png', 'path': 'image/plate_UNREL2.png'},
    {'name': 'image/coatNEU_posSOA.png', 'path': 'image/coatNEU_posSOA.png'},
    {'name': 'image/coatNEU_posSOA2.png', 'path': 'image/coatNEU_posSOA2.png'},
    {'name': 'image/noseUNREL_negSOA.png', 'path': 'image/noseUNREL_negSOA.png'},
    {'name': 'image/noseUNREL_negSOA2.png', 'path': 'image/noseUNREL_negSOA2.png'},
    {'name': 'image/wardrobe_ID.png', 'path': 'image/wardrobe_ID.png'},
    {'name': 'image/wardrobe_ID2.png', 'path': 'image/wardrobe_ID2.png'},
    {'name': 'image/deer_NEU.png', 'path': 'image/deer_NEU.png'},
    {'name': 'image/deer_NEU2.png', 'path': 'image/deer_NEU2.png'},
    {'name': 'image/bikeUNREL_negSOA.png', 'path': 'image/bikeUNREL_negSOA.png'},
    {'name': 'image/bikeUNREL_negSOA2.png', 'path': 'image/bikeUNREL_negSOA2.png'},
    {'name': 'image/glassUNREL_posSOA.png', 'path': 'image/glassUNREL_posSOA.png'},
    {'name': 'image/glassUNREL_posSOA2.png', 'path': 'image/glassUNREL_posSOA2.png'},
    {'name': 'image/leg_UNREL.png', 'path': 'image/leg_UNREL.png'},
    {'name': 'image/leg_UNREL2.png', 'path': 'image/leg_UNREL2.png'},
    {'name': 'image/plane_NEU.png', 'path': 'image/plane_NEU.png'},
    {'name': 'image/plane_NEU2.png', 'path': 'image/plane_NEU2.png'},
    {'name': 'image/church_REL.png', 'path': 'image/church_REL.png'},
    {'name': 'image/church_REL2.png', 'path': 'image/church_REL2.png'},
    {'name': 'image/table_ID.png', 'path': 'image/table_ID.png'},
    {'name': 'image/table_ID2.png', 'path': 'image/table_ID2.png'},
    {'name': 'image/churchREL_posSOA.png', 'path': 'image/churchREL_posSOA.png'},
    {'name': 'image/churchREL_posSOA2.png', 'path': 'image/churchREL_posSOA2.png'},
    {'name': 'image/tortoise_ID.png', 'path': 'image/tortoise_ID.png'},
    {'name': 'image/tortoise_ID2.png', 'path': 'image/tortoise_ID2.png'},
    {'name': 'image/churchNEU_posSOA.png', 'path': 'image/churchNEU_posSOA.png'},
    {'name': 'image/churchNEU_posSOA2.png', 'path': 'image/churchNEU_posSOA2.png'},
    {'name': 'image/bike_REL.png', 'path': 'image/bike_REL.png'},
    {'name': 'image/bike_REL2.png', 'path': 'image/bike_REL2.png'},
    {'name': 'image/swordID_posSOA.png', 'path': 'image/swordID_posSOA.png'},
    {'name': 'image/swordID_posSOA2.png', 'path': 'image/swordID_posSOA2.png'},
    {'name': 'image/castleUNREL_posSOA.png', 'path': 'image/castleUNREL_posSOA.png'},
    {'name': 'image/castleUNREL_posSOA2.png', 'path': 'image/castleUNREL_posSOA2.png'},
    {'name': 'image/planeNEU_posSOA.png', 'path': 'image/planeNEU_posSOA.png'},
    {'name': 'image/planeNEU_posSOA2.png', 'path': 'image/planeNEU_posSOA2.png'},
    {'name': 'image/factory_NEU.png', 'path': 'image/factory_NEU.png'},
    {'name': 'image/factory_NEU2.png', 'path': 'image/factory_NEU2.png'},
    {'name': 'image/wardrobe_UNREL.png', 'path': 'image/wardrobe_UNREL.png'},
    {'name': 'image/wardrobe_UNREL2.png', 'path': 'image/wardrobe_UNREL2.png'},
    {'name': 'image/plane_ID.png', 'path': 'image/plane_ID.png'},
    {'name': 'image/plane_ID2.png', 'path': 'image/plane_ID2.png'},
    {'name': 'image/dagger_REL.png', 'path': 'image/dagger_REL.png'},
    {'name': 'image/dagger_REL2.png', 'path': 'image/dagger_REL2.png'},
    {'name': 'image/factory_ID.png', 'path': 'image/factory_ID.png'},
    {'name': 'image/factory_ID2.png', 'path': 'image/factory_ID2.png'},
    {'name': 'image/tableID_negSOA.png', 'path': 'image/tableID_negSOA.png'},
    {'name': 'image/tableID_negSOA2.png', 'path': 'image/tableID_negSOA2.png'},
    {'name': 'image/cannon_ID.png', 'path': 'image/cannon_ID.png'},
    {'name': 'image/cannon_ID2.png', 'path': 'image/cannon_ID2.png'},
    {'name': 'image/carREL_negSOA.png', 'path': 'image/carREL_negSOA.png'},
    {'name': 'image/carREL_negSOA2.png', 'path': 'image/carREL_negSOA2.png'},
    {'name': 'image/planeUNREL_negSOA.png', 'path': 'image/planeUNREL_negSOA.png'},
    {'name': 'image/planeUNREL_negSOA2.png', 'path': 'image/planeUNREL_negSOA2.png'},
    {'name': 'image/castle_REL.png', 'path': 'image/castle_REL.png'},
    {'name': 'image/castle_REL2.png', 'path': 'image/castle_REL2.png'},
    {'name': 'image/nose_UNREL.png', 'path': 'image/nose_UNREL.png'},
    {'name': 'image/nose_UNREL2.png', 'path': 'image/nose_UNREL2.png'},
    {'name': 'image/train_NEU.png', 'path': 'image/train_NEU.png'},
    {'name': 'image/train_NEU2.png', 'path': 'image/train_NEU2.png'},
    {'name': 'image/cup_REL.png', 'path': 'image/cup_REL.png'},
    {'name': 'image/cup_REL2.png', 'path': 'image/cup_REL2.png'},
    {'name': 'image/deerID_posSOA.png', 'path': 'image/deerID_posSOA.png'},
    {'name': 'image/deerID_posSOA2.png', 'path': 'image/deerID_posSOA2.png'},
    {'name': 'image/table_REL.png', 'path': 'image/table_REL.png'},
    {'name': 'image/table_REL2.png', 'path': 'image/table_REL2.png'},
    {'name': 'image/planeNEU_negSOA.png', 'path': 'image/planeNEU_negSOA.png'},
    {'name': 'image/planeNEU_negSOA2.png', 'path': 'image/planeNEU_negSOA2.png'},
    {'name': 'image/jug_UNREL.png', 'path': 'image/jug_UNREL.png'},
    {'name': 'image/jug_UNREL2.png', 'path': 'image/jug_UNREL2.png'},
    {'name': 'image/coat_REL.png', 'path': 'image/coat_REL.png'},
    {'name': 'image/coat_REL2.png', 'path': 'image/coat_REL2.png'},
    {'name': 'image/bedREL_posSOA.png', 'path': 'image/bedREL_posSOA.png'},
    {'name': 'image/bedREL_posSOA2.png', 'path': 'image/bedREL_posSOA2.png'},
    {'name': 'image/factoryREL_negSOA.png', 'path': 'image/factoryREL_negSOA.png'},
    {'name': 'image/factoryREL_negSOA2.png', 'path': 'image/factoryREL_negSOA2.png'},
    {'name': 'image/castleNEU_negSOA.png', 'path': 'image/castleNEU_negSOA.png'},
    {'name': 'image/castleNEU_negSOA2.png', 'path': 'image/castleNEU_negSOA2.png'},
    {'name': 'exp_items_s4.csv', 'path': 'exp_items_s4.csv'},
    {'name': 'image/deskREL_negSOA.png', 'path': 'image/deskREL_negSOA.png'},
    {'name': 'image/deskREL_negSOA2.png', 'path': 'image/deskREL_negSOA2.png'},
    {'name': 'image/noseUNREL_posSOA.png', 'path': 'image/noseUNREL_posSOA.png'},
    {'name': 'image/noseUNREL_posSOA2.png', 'path': 'image/noseUNREL_posSOA2.png'},
    {'name': 'image/coatNEU_negSOA.png', 'path': 'image/coatNEU_negSOA.png'},
    {'name': 'image/coatNEU_negSOA2.png', 'path': 'image/coatNEU_negSOA2.png'},
    {'name': 'image/windmillUNREL_posSOA.png', 'path': 'image/windmillUNREL_posSOA.png'},
    {'name': 'image/windmillUNREL_posSOA2.png', 'path': 'image/windmillUNREL_posSOA2.png'},
    {'name': 'image/rabbitID_negSOA.png', 'path': 'image/rabbitID_negSOA.png'},
    {'name': 'image/rabbitID_negSOA2.png', 'path': 'image/rabbitID_negSOA2.png'},
    {'name': 'image/cupNEU_negSOA.png', 'path': 'image/cupNEU_negSOA.png'},
    {'name': 'image/cupNEU_negSOA2.png', 'path': 'image/cupNEU_negSOA2.png'},
    {'name': 'image/swordREL_negSOA.png', 'path': 'image/swordREL_negSOA.png'},
    {'name': 'image/swordREL_negSOA2.png', 'path': 'image/swordREL_negSOA2.png'},
    {'name': 'image/earUNREL_negSOA.png', 'path': 'image/earUNREL_negSOA.png'},
    {'name': 'image/earUNREL_negSOA2.png', 'path': 'image/earUNREL_negSOA2.png'},
    {'name': 'image/carNEU_negSOA.png', 'path': 'image/carNEU_negSOA.png'},
    {'name': 'image/carNEU_negSOA2.png', 'path': 'image/carNEU_negSOA2.png'},
    {'name': 'image/bike_UNREL.png', 'path': 'image/bike_UNREL.png'},
    {'name': 'image/bike_UNREL2.png', 'path': 'image/bike_UNREL2.png'},
    {'name': 'image/pistol_REL.png', 'path': 'image/pistol_REL.png'},
    {'name': 'image/pistol_REL2.png', 'path': 'image/pistol_REL2.png'},
    {'name': 'image/wardrobeUNREL_negSOA.png', 'path': 'image/wardrobeUNREL_negSOA.png'},
    {'name': 'image/wardrobeUNREL_negSOA2.png', 'path': 'image/wardrobeUNREL_negSOA2.png'},
    {'name': 'image/carNEU_posSOA.png', 'path': 'image/carNEU_posSOA.png'},
    {'name': 'image/carNEU_posSOA2.png', 'path': 'image/carNEU_posSOA2.png'},
    {'name': 'image/factoryUNREL_negSOA.png', 'path': 'image/factoryUNREL_negSOA.png'},
    {'name': 'image/factoryUNREL_negSOA2.png', 'path': 'image/factoryUNREL_negSOA2.png'},
    {'name': 'image/skirtUNREL_negSOA.png', 'path': 'image/skirtUNREL_negSOA.png'},
    {'name': 'image/skirtUNREL_negSOA2.png', 'path': 'image/skirtUNREL_negSOA2.png'},
    {'name': 'image/desk_UNREL.png', 'path': 'image/desk_UNREL.png'},
    {'name': 'image/desk_UNREL2.png', 'path': 'image/desk_UNREL2.png'},
    {'name': 'image/wardrobeREL_posSOA.png', 'path': 'image/wardrobeREL_posSOA.png'},
    {'name': 'image/wardrobeREL_posSOA2.png', 'path': 'image/wardrobeREL_posSOA2.png'},
    {'name': 'image/cup_ID.png', 'path': 'image/cup_ID.png'},
    {'name': 'image/cup_ID2.png', 'path': 'image/cup_ID2.png'},
    {'name': 'image/noseID_negSOA.png', 'path': 'image/noseID_negSOA.png'},
    {'name': 'image/noseID_negSOA2.png', 'path': 'image/noseID_negSOA2.png'},
    {'name': 'image/castle_NEU.png', 'path': 'image/castle_NEU.png'},
    {'name': 'image/castle_NEU2.png', 'path': 'image/castle_NEU2.png'},
    {'name': 'image/cannon_UNREL.png', 'path': 'image/cannon_UNREL.png'},
    {'name': 'image/cannon_UNREL2.png', 'path': 'image/cannon_UNREL2.png'},
    {'name': 'image/churchUNREL_posSOA.png', 'path': 'image/churchUNREL_posSOA.png'},
    {'name': 'image/churchUNREL_posSOA2.png', 'path': 'image/churchUNREL_posSOA2.png'},
    {'name': 'image/plate_NEU.png', 'path': 'image/plate_NEU.png'},
    {'name': 'image/plate_NEU2.png', 'path': 'image/plate_NEU2.png'},
    {'name': 'image/deskUNREL_posSOA.png', 'path': 'image/deskUNREL_posSOA.png'},
    {'name': 'image/deskUNREL_posSOA2.png', 'path': 'image/deskUNREL_posSOA2.png'},
    {'name': 'image/swordID_negSOA.png', 'path': 'image/swordID_negSOA.png'},
    {'name': 'image/swordID_negSOA2.png', 'path': 'image/swordID_negSOA2.png'},
    {'name': 'image/glass_UNREL.png', 'path': 'image/glass_UNREL.png'},
    {'name': 'image/glass_UNREL2.png', 'path': 'image/glass_UNREL2.png'},
    {'name': 'image/windmill_UNREL.png', 'path': 'image/windmill_UNREL.png'},
    {'name': 'image/windmill_UNREL2.png', 'path': 'image/windmill_UNREL2.png'},
    {'name': 'image/skirt_UNREL.png', 'path': 'image/skirt_UNREL.png'},
    {'name': 'image/skirt_UNREL2.png', 'path': 'image/skirt_UNREL2.png'},
    {'name': 'image/car_NEU.png', 'path': 'image/car_NEU.png'},
    {'name': 'image/car_NEU2.png', 'path': 'image/car_NEU2.png'},
    {'name': 'image/cupREL_negSOA.png', 'path': 'image/cupREL_negSOA.png'},
    {'name': 'image/cupREL_negSOA2.png', 'path': 'image/cupREL_negSOA2.png'},
    {'name': 'image/pistolID_posSOA.png', 'path': 'image/pistolID_posSOA.png'},
    {'name': 'image/pistolID_posSOA2.png', 'path': 'image/pistolID_posSOA2.png'},
    {'name': 'image/windmill_NEU.png', 'path': 'image/windmill_NEU.png'},
    {'name': 'image/windmill_NEU2.png', 'path': 'image/windmill_NEU2.png'},
    {'name': 'image/castleID_negSOA.png', 'path': 'image/castleID_negSOA.png'},
    {'name': 'image/castleID_negSOA2.png', 'path': 'image/castleID_negSOA2.png'},
    {'name': 'image/rabbitNEU_posSOA.png', 'path': 'image/rabbitNEU_posSOA.png'},
    {'name': 'image/rabbitNEU_posSOA2.png', 'path': 'image/rabbitNEU_posSOA2.png'},
    {'name': 'image/jugUNREL_posSOA.png', 'path': 'image/jugUNREL_posSOA.png'},
    {'name': 'image/jugUNREL_posSOA2.png', 'path': 'image/jugUNREL_posSOA2.png'},
    {'name': 'image/swan_NEU.png', 'path': 'image/swan_NEU.png'},
    {'name': 'image/swan_NEU2.png', 'path': 'image/swan_NEU2.png'},
    {'name': 'image/deerUNREL_posSOA.png', 'path': 'image/deerUNREL_posSOA.png'},
    {'name': 'image/deerUNREL_posSOA2.png', 'path': 'image/deerUNREL_posSOA2.png'},
    {'name': 'image/glassID_posSOA.png', 'path': 'image/glassID_posSOA.png'},
    {'name': 'image/glassID_posSOA2.png', 'path': 'image/glassID_posSOA2.png'},
    {'name': 'image/bikeNEU_negSOA.png', 'path': 'image/bikeNEU_negSOA.png'},
    {'name': 'image/bikeNEU_negSOA2.png', 'path': 'image/bikeNEU_negSOA2.png'},
    {'name': 'image/cannonID_posSOA.png', 'path': 'image/cannonID_posSOA.png'},
    {'name': 'image/cannonID_posSOA2.png', 'path': 'image/cannonID_posSOA2.png'},
    {'name': 'image/factoryREL_posSOA.png', 'path': 'image/factoryREL_posSOA.png'},
    {'name': 'image/factoryREL_posSOA2.png', 'path': 'image/factoryREL_posSOA2.png'},
    {'name': 'image/tortoise_UNREL.png', 'path': 'image/tortoise_UNREL.png'},
    {'name': 'image/tortoise_UNREL2.png', 'path': 'image/tortoise_UNREL2.png'},
    {'name': 'image/jug_REL.png', 'path': 'image/jug_REL.png'},
    {'name': 'image/jug_REL2.png', 'path': 'image/jug_REL2.png'},
    {'name': 'image/sweater_NEU.png', 'path': 'image/sweater_NEU.png'},
    {'name': 'image/sweater_NEU2.png', 'path': 'image/sweater_NEU2.png'},
    {'name': 'image/bedREL_negSOA.png', 'path': 'image/bedREL_negSOA.png'},
    {'name': 'image/bedREL_negSOA2.png', 'path': 'image/bedREL_negSOA2.png'},
    {'name': 'image/swordREL_posSOA.png', 'path': 'image/swordREL_posSOA.png'},
    {'name': 'image/swordREL_posSOA2.png', 'path': 'image/swordREL_posSOA2.png'},
    {'name': 'image/castleID_posSOA.png', 'path': 'image/castleID_posSOA.png'},
    {'name': 'image/castleID_posSOA2.png', 'path': 'image/castleID_posSOA2.png'},
    {'name': 'image/vest_NEU.png', 'path': 'image/vest_NEU.png'},
    {'name': 'image/vest_NEU2.png', 'path': 'image/vest_NEU2.png'},
    {'name': 'image/deerNEU_negSOA.png', 'path': 'image/deerNEU_negSOA.png'},
    {'name': 'image/deerNEU_negSOA2.png', 'path': 'image/deerNEU_negSOA2.png'},
    {'name': 'image/pistolREL_negSOA.png', 'path': 'image/pistolREL_negSOA.png'},
    {'name': 'image/pistolREL_negSOA2.png', 'path': 'image/pistolREL_negSOA2.png'},
    {'name': 'image/bed_ID.png', 'path': 'image/bed_ID.png'},
    {'name': 'image/bed_ID2.png', 'path': 'image/bed_ID2.png'},
    {'name': 'image/sword_NEU.png', 'path': 'image/sword_NEU.png'},
    {'name': 'image/sword_NEU2.png', 'path': 'image/sword_NEU2.png'},
    {'name': 'image/cannonUNREL_negSOA.png', 'path': 'image/cannonUNREL_negSOA.png'},
    {'name': 'image/cannonUNREL_negSOA2.png', 'path': 'image/cannonUNREL_negSOA2.png'},
    {'name': 'image/factory_UNREL.png', 'path': 'image/factory_UNREL.png'},
    {'name': 'image/factory_UNREL2.png', 'path': 'image/factory_UNREL2.png'},
    {'name': 'image/coatID_posSOA.png', 'path': 'image/coatID_posSOA.png'},
    {'name': 'image/coatID_posSOA2.png', 'path': 'image/coatID_posSOA2.png'},
    {'name': 'image/vestUNREL_posSOA.png', 'path': 'image/vestUNREL_posSOA.png'},
    {'name': 'image/vestUNREL_posSOA2.png', 'path': 'image/vestUNREL_posSOA2.png'},
    {'name': 'image/sweater_ID.png', 'path': 'image/sweater_ID.png'},
    {'name': 'image/sweater_ID2.png', 'path': 'image/sweater_ID2.png'},
    {'name': 'image/deerID_negSOA.png', 'path': 'image/deerID_negSOA.png'},
    {'name': 'image/deerID_negSOA2.png', 'path': 'image/deerID_negSOA2.png'},
    {'name': 'image/vest_UNREL.png', 'path': 'image/vest_UNREL.png'},
    {'name': 'image/vest_UNREL2.png', 'path': 'image/vest_UNREL2.png'},
    {'name': 'image/tortoise_REL.png', 'path': 'image/tortoise_REL.png'},
    {'name': 'image/tortoise_REL2.png', 'path': 'image/tortoise_REL2.png'},
    {'name': 'image/coatNEU_posSOA.png', 'path': 'image/coatNEU_posSOA.png'},
    {'name': 'image/coatNEU_posSOA2.png', 'path': 'image/coatNEU_posSOA2.png'},
    {'name': 'image/ear_UNREL.png', 'path': 'image/ear_UNREL.png'},
    {'name': 'image/ear_UNREL2.png', 'path': 'image/ear_UNREL2.png'},
    {'name': 'image/sword_ID.png', 'path': 'image/sword_ID.png'},
    {'name': 'image/sword_ID2.png', 'path': 'image/sword_ID2.png'},
    {'name': 'image/earID_negSOA.png', 'path': 'image/earID_negSOA.png'},
    {'name': 'image/earID_negSOA2.png', 'path': 'image/earID_negSOA2.png'},
    {'name': 'image/rabbit_ID.png', 'path': 'image/rabbit_ID.png'},
    {'name': 'image/rabbit_ID2.png', 'path': 'image/rabbit_ID2.png'},
    {'name': 'image/deer_NEU.png', 'path': 'image/deer_NEU.png'},
    {'name': 'image/deer_NEU2.png', 'path': 'image/deer_NEU2.png'},
    {'name': 'image/tortoiseREL_negSOA.png', 'path': 'image/tortoiseREL_negSOA.png'},
    {'name': 'image/tortoiseREL_negSOA2.png', 'path': 'image/tortoiseREL_negSOA2.png'},
    {'name': 'image/jugID_negSOA.png', 'path': 'image/jugID_negSOA.png'},
    {'name': 'image/jugID_negSOA2.png', 'path': 'image/jugID_negSOA2.png'},
    {'name': 'image/sweater_UNREL.png', 'path': 'image/sweater_UNREL.png'},
    {'name': 'image/sweater_UNREL2.png', 'path': 'image/sweater_UNREL2.png'},
    {'name': 'image/train_ID.png', 'path': 'image/train_ID.png'},
    {'name': 'image/train_ID2.png', 'path': 'image/train_ID2.png'},
    {'name': 'image/plane_NEU.png', 'path': 'image/plane_NEU.png'},
    {'name': 'image/plane_NEU2.png', 'path': 'image/plane_NEU2.png'},
    {'name': 'image/desk_REL.png', 'path': 'image/desk_REL.png'},
    {'name': 'image/desk_REL2.png', 'path': 'image/desk_REL2.png'},
    {'name': 'image/plateID_posSOA.png', 'path': 'image/plateID_posSOA.png'},
    {'name': 'image/plateID_posSOA2.png', 'path': 'image/plateID_posSOA2.png'},
    {'name': 'image/churchNEU_posSOA.png', 'path': 'image/churchNEU_posSOA.png'},
    {'name': 'image/churchNEU_posSOA2.png', 'path': 'image/churchNEU_posSOA2.png'},
    {'name': 'image/deskID_posSOA.png', 'path': 'image/deskID_posSOA.png'},
    {'name': 'image/deskID_posSOA2.png', 'path': 'image/deskID_posSOA2.png'},
    {'name': 'image/swanREL_negSOA.png', 'path': 'image/swanREL_negSOA.png'},
    {'name': 'image/swanREL_negSOA2.png', 'path': 'image/swanREL_negSOA2.png'},
    {'name': 'image/swordUNREL_negSOA.png', 'path': 'image/swordUNREL_negSOA.png'},
    {'name': 'image/swordUNREL_negSOA2.png', 'path': 'image/swordUNREL_negSOA2.png'},
    {'name': 'image/coatREL_negSOA.png', 'path': 'image/coatREL_negSOA.png'},
    {'name': 'image/coatREL_negSOA2.png', 'path': 'image/coatREL_negSOA2.png'},
    {'name': 'image/factory_NEU.png', 'path': 'image/factory_NEU.png'},
    {'name': 'image/factory_NEU2.png', 'path': 'image/factory_NEU2.png'},
    {'name': 'image/planeREL_negSOA.png', 'path': 'image/planeREL_negSOA.png'},
    {'name': 'image/planeREL_negSOA2.png', 'path': 'image/planeREL_negSOA2.png'},
    {'name': 'image/factory_REL.png', 'path': 'image/factory_REL.png'},
    {'name': 'image/factory_REL2.png', 'path': 'image/factory_REL2.png'},
    {'name': 'image/planeNEU_posSOA.png', 'path': 'image/planeNEU_posSOA.png'},
    {'name': 'image/planeNEU_posSOA2.png', 'path': 'image/planeNEU_posSOA2.png'},
    {'name': 'image/sweaterUNREL_posSOA.png', 'path': 'image/sweaterUNREL_posSOA.png'},
    {'name': 'image/sweaterUNREL_posSOA2.png', 'path': 'image/sweaterUNREL_posSOA2.png'},
    {'name': 'image/tortoiseID_negSOA.png', 'path': 'image/tortoiseID_negSOA.png'},
    {'name': 'image/tortoiseID_negSOA2.png', 'path': 'image/tortoiseID_negSOA2.png'},
    {'name': 'image/train_NEU.png', 'path': 'image/train_NEU.png'},
    {'name': 'image/train_NEU2.png', 'path': 'image/train_NEU2.png'},
    {'name': 'image/planeID_negSOA.png', 'path': 'image/planeID_negSOA.png'},
    {'name': 'image/planeID_negSOA2.png', 'path': 'image/planeID_negSOA2.png'},
    {'name': 'image/cupID_posSOA.png', 'path': 'image/cupID_posSOA.png'},
    {'name': 'image/cupID_posSOA2.png', 'path': 'image/cupID_posSOA2.png'},
    {'name': 'image/ear_REL.png', 'path': 'image/ear_REL.png'},
    {'name': 'image/ear_REL2.png', 'path': 'image/ear_REL2.png'},
    {'name': 'image/planeNEU_negSOA.png', 'path': 'image/planeNEU_negSOA.png'},
    {'name': 'image/planeNEU_negSOA2.png', 'path': 'image/planeNEU_negSOA2.png'},
    {'name': 'image/vestID_negSOA.png', 'path': 'image/vestID_negSOA.png'},
    {'name': 'image/vestID_negSOA2.png', 'path': 'image/vestID_negSOA2.png'},
    {'name': 'image/pistolREL_posSOA.png', 'path': 'image/pistolREL_posSOA.png'},
    {'name': 'image/pistolREL_posSOA2.png', 'path': 'image/pistolREL_posSOA2.png'},
    {'name': 'image/daggerREL_negSOA.png', 'path': 'image/daggerREL_negSOA.png'},
    {'name': 'image/daggerREL_negSOA2.png', 'path': 'image/daggerREL_negSOA2.png'},
    {'name': 'image/castleNEU_negSOA.png', 'path': 'image/castleNEU_negSOA.png'},
    {'name': 'image/castleNEU_negSOA2.png', 'path': 'image/castleNEU_negSOA2.png'},
    {'name': 'image/skirtID_negSOA.png', 'path': 'image/skirtID_negSOA.png'},
    {'name': 'image/skirtID_negSOA2.png', 'path': 'image/skirtID_negSOA2.png'},
    {'name': 'image/tableUNREL_posSOA.png', 'path': 'image/tableUNREL_posSOA.png'},
    {'name': 'image/tableUNREL_posSOA2.png', 'path': 'image/tableUNREL_posSOA2.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.2';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var welcomeClock;
var textWelcome;
var key_respWelcome;
var blank500Clock;
var text;
var familiarIntroClock;
var familiarization_intro;
var familiarization_keyresp;
var NamingIntroClock;
var NamingInstruct_text;
var NamingInstruct_keyresp;
var practiceTrialInstructionsClock;
var PTInstruct_text;
var PTInstruct_keyresp;
var TrialInstructionsClock;
var TrialInstruct_text;
var TrialInstruct_keyresp;
var Trial_Set_1Clock;
var Fixation_Set_1;
var image_2_set_1;
var image_1_set_1;
var Recording_Circle_Set_1;
var Enter_Text_Set_1;
var Enter_Response_Set_1;
var betweentrialbreakClock;
var text_6;
var key_resp;
var ten;
var nine;
var eight;
var seven;
var six;
var five;
var four;
var three;
var two;
var one;
var text_16end;
var NewSetBeginClock;
var text_NewSet;
var Trial_Set_2Clock;
var Fixation_Set_2;
var image_2_set_2;
var image_1_set_2;
var Recording_Circle_Set_2;
var Enter_Text_Set_2;
var Enter_Response_Set_2;
var Trial_Set_3Clock;
var Fixation_Set_3;
var image_2_set_3;
var image_1_set_3;
var Recording_Circle_Set_3;
var Enter_Text_Set_3;
var Enter_Response_Set_3;
var Trial_Set_4Clock;
var Fixation_Set_4;
var image_2_set_4;
var image_1_set_4;
var Recording_Circle_Set_4;
var Enter_Text_Set_4;
var Enter_Response_Set_4;
var goodbyeClock;
var textGoodbye;
var key_resp_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: 'Welcome!\n\nThe experiment will consist of four phases: a familiarization phase, a familiarization check, a practice trial, and experimental trials.\n\nDuring the familiarization phase, multiple single object images will be presented. You will be expected to familiarize yourself with the names of these images. Press enter when ready to move to the next screen. \n\nYou will then move on to a familiarization exercise to ensure you can correctly identify the names of these images.\n\nEach practice and experimental trial will begin with a red fixation cross that will remain on the screen for 300 ms. After the cross disappears, an image of a single object will appear superimposed with some text. Below the image, you will see a red dot indicating the microphone is ready to record. \n\nPlease say the name of the image as quickly as possible. This name should match the object name provided during the familiarization exercise. \n\nWhen finished stating the name, press enter to move to the next trial.\n\nYou will be reminded of these instructions prior to the start of the trials.\n\nIf at any time you need technical assistance or any questions/concerns, please contact the research assistant.\n\nPress enter when ready',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_respWelcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blank500"
  blank500Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "familiarIntro"
  familiarIntroClock = new util.Clock();
  familiarization_intro = new visual.TextStim({
    win: psychoJS.window,
    name: 'familiarization_intro',
    text: 'The familiarization stage will now begin.\n\nRemember to take your time and familiarize yourself with the name of each object. You will be asked to name these items in the trial.\n\nPress enter when ready to begin.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  familiarization_keyresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "NamingIntro"
  NamingIntroClock = new util.Clock();
  NamingInstruct_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'NamingInstruct_text',
    text: 'This is the familiarization check \n\nAn image will appear on the screen. Please say the name of the image as quickly as possible. This familiarization check is about making sure you know the name of the object in the image.\n\nThe correct name of the image will appear on the screen after 3 seconds.\n\nPress enter when ready to begin.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  NamingInstruct_keyresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practiceTrialInstructions"
  practiceTrialInstructionsClock = new util.Clock();
  PTInstruct_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'PTInstruct_text',
    text: 'PRACTICE TRIAL INSTRUCTIONS\n\nEach trial will begin with a red fixation cross that will remain on the screen for 300 ms. After the cross disappears, an image of a single object will appear superimposed with some text. Below the image, you will see a red dot indicating the microphone is ready to record. \n\nPlease say the name of the image as quickly as possible. This name should match the object name provided during the familiarization exercise. \n\nWhen finished stating the name, press enter to move to the next trial.\n\nIf at any time you need technical assistance or any questions/concerns, please contact the research assistant.\n\nThe practice trial will now begin.\nPress enter when ready',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  PTInstruct_keyresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "TrialInstructions"
  TrialInstructionsClock = new util.Clock();
  TrialInstruct_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialInstruct_text',
    text: 'TRIAL INSTRUCTIONS\n\nEach trial will begin with a red fixation cross that will remain on the screen for 300 ms. After the cross disappears, an image of a single object will appear superimposed with some text. Below the image, you will see a red dot indicating the microphone is ready to record. \n\nPlease say the name of the image as quickly as possible. This name should match the object name provided during the familiarization exercise. \n\nWhen finished stating the name, press enter to move to the next trial.\n\nThroughout the experiment, will receive seven 1 minute breaks that may be skipped at your discretion. \n\nIf at any time you need technical assitance or any questions/concerns, please contact the research assistant.\n\nThe trial will now begin\nPress enter when ready',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  TrialInstruct_keyresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Trial_Set_1"
  Trial_Set_1Clock = new util.Clock();
  Fixation_Set_1 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Fixation_Set_1', 
    vertices: 'cross', size:[0.4, 0.4],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: [0.6627, (- 1.0), (- 1.0)],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  image_2_set_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2_set_1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_1_set_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_1_set_1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Recording_Circle_Set_1 = new visual.Polygon({
    win: psychoJS.window, name: 'Recording_Circle_Set_1', 
    edges: 100, size:[0.05, 0.05],
    ori: 0.0, 
    pos: [0, (- 0.35)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: [0.6627, (- 1.0), (- 1.0)],
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  Enter_Text_Set_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Enter_Text_Set_1',
    text: '',
    font: 'Verdana',
    units: undefined, 
    pos: [0, (- 0.45)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -4.0 
  });
  
  Enter_Response_Set_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "betweentrialbreak"
  betweentrialbreakClock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'You are done with that set. \nYou may now take up to a 1 minute rest.\nA countdown will appear when the experiment is close.\nPress enter at any time to bypass this break',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.25], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  ten = new visual.TextStim({
    win: psychoJS.window,
    name: 'ten',
    text: '10',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.06)], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.8431, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -2.0 
  });
  
  nine = new visual.TextStim({
    win: psychoJS.window,
    name: 'nine',
    text: '9',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.06)], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.8431, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -3.0 
  });
  
  eight = new visual.TextStim({
    win: psychoJS.window,
    name: 'eight',
    text: '8',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.06)], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.8431, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -4.0 
  });
  
  seven = new visual.TextStim({
    win: psychoJS.window,
    name: 'seven',
    text: '7',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.06)], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.8431, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -5.0 
  });
  
  six = new visual.TextStim({
    win: psychoJS.window,
    name: 'six',
    text: '6',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.06)], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.8431, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -6.0 
  });
  
  five = new visual.TextStim({
    win: psychoJS.window,
    name: 'five',
    text: '5',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.06)], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.8431, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -7.0 
  });
  
  four = new visual.TextStim({
    win: psychoJS.window,
    name: 'four',
    text: '4',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.06)], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.8431, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -8.0 
  });
  
  three = new visual.TextStim({
    win: psychoJS.window,
    name: 'three',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.06)], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.8431, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -9.0 
  });
  
  two = new visual.TextStim({
    win: psychoJS.window,
    name: 'two',
    text: '2',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.06)], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.8431, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -10.0 
  });
  
  one = new visual.TextStim({
    win: psychoJS.window,
    name: 'one',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.06)], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.8431, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -11.0 
  });
  
  text_16end = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_16end',
    text: 'PRESS ENTER NOW',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.06)], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -12.0 
  });
  
  // Initialize components for Routine "NewSetBegin"
  NewSetBeginClock = new util.Clock();
  text_NewSet = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_NewSet',
    text: 'The next trial is begining now',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Trial_Set_2"
  Trial_Set_2Clock = new util.Clock();
  Fixation_Set_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Fixation_Set_2', 
    vertices: 'cross', size:[0.4, 0.4],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: [0.6627, (- 1.0), (- 1.0)],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  image_2_set_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2_set_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_1_set_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_1_set_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Recording_Circle_Set_2 = new visual.Polygon({
    win: psychoJS.window, name: 'Recording_Circle_Set_2', 
    edges: 100, size:[0.05, 0.05],
    ori: 0.0, 
    pos: [0, (- 0.35)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: [0.6627, (- 1.0), (- 1.0)],
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  Enter_Text_Set_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Enter_Text_Set_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  Enter_Response_Set_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Trial_Set_3"
  Trial_Set_3Clock = new util.Clock();
  Fixation_Set_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Fixation_Set_3', 
    vertices: 'cross', size:[0.4, 0.4],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: [0.6627, (- 1.0), (- 1.0)],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  image_2_set_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2_set_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_1_set_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_1_set_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Recording_Circle_Set_3 = new visual.Polygon({
    win: psychoJS.window, name: 'Recording_Circle_Set_3', 
    edges: 100, size:[0.05, 0.05],
    ori: 0.0, 
    pos: [0, (- 0.35)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: [0.6627, (- 1.0), (- 1.0)],
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  Enter_Text_Set_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Enter_Text_Set_3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  Enter_Response_Set_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Trial_Set_4"
  Trial_Set_4Clock = new util.Clock();
  Fixation_Set_4 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Fixation_Set_4', 
    vertices: 'cross', size:[0.4, 0.4],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: [0.6627, (- 1.0), (- 1.0)],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  image_2_set_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2_set_4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_1_set_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_1_set_4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Recording_Circle_Set_4 = new visual.Polygon({
    win: psychoJS.window, name: 'Recording_Circle_Set_4', 
    edges: 100, size:[0.05, 0.05],
    ori: 0.0, 
    pos: [0, (- 0.35)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: new util.Color([0.6627, (- 1.0), (- 1.0)]),
    fillColor: [0.6627, (- 1.0), (- 1.0)],
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  Enter_Text_Set_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Enter_Text_Set_4',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  Enter_Response_Set_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "goodbye"
  goodbyeClock = new util.Clock();
  textGoodbye = new visual.TextStim({
    win: psychoJS.window,
    name: 'textGoodbye',
    text: 'The experiment is over.\n\nThank you for participating.\nIf you have any questions or concerns, you may email\nRichard Futrell\nIRB\n\nPress enter to end',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var welcomeMaxDurationReached;
var _key_respWelcome_allKeys;
var welcomeMaxDuration;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    welcomeMaxDurationReached = false;
    // update component parameters for each repeat
    key_respWelcome.keys = undefined;
    key_respWelcome.rt = undefined;
    _key_respWelcome_allKeys = [];
    psychoJS.experiment.addData('welcome.started', globalClock.getTime());
    welcomeMaxDuration = null
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(textWelcome);
    welcomeComponents.push(key_respWelcome);
    
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWelcome* updates
    if (t >= 0.0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWelcome.tStart = t;  // (not accounting for frame time here)
      textWelcome.frameNStart = frameN;  // exact frame index
      
      textWelcome.setAutoDraw(true);
    }
    
    
    // *key_respWelcome* updates
    if (t >= 0.0 && key_respWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respWelcome.tStart = t;  // (not accounting for frame time here)
      key_respWelcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respWelcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respWelcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respWelcome.clearEvents(); });
    }
    
    if (key_respWelcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respWelcome.getKeys({keyList: ['return'], waitRelease: false});
      _key_respWelcome_allKeys = _key_respWelcome_allKeys.concat(theseKeys);
      if (_key_respWelcome_allKeys.length > 0) {
        key_respWelcome.keys = _key_respWelcome_allKeys[_key_respWelcome_allKeys.length - 1].name;  // just the last key pressed
        key_respWelcome.rt = _key_respWelcome_allKeys[_key_respWelcome_allKeys.length - 1].rt;
        key_respWelcome.duration = _key_respWelcome_allKeys[_key_respWelcome_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    welcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respWelcome.corr, level);
    }
    psychoJS.experiment.addData('key_respWelcome.keys', key_respWelcome.keys);
    if (typeof key_respWelcome.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respWelcome.rt', key_respWelcome.rt);
        psychoJS.experiment.addData('key_respWelcome.duration', key_respWelcome.duration);
        routineTimer.reset();
        }
    
    key_respWelcome.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blank500MaxDurationReached;
var blank500MaxDuration;
var blank500Components;
function blank500RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blank500' ---
    t = 0;
    blank500Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    blank500MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('blank500.started', globalClock.getTime());
    blank500MaxDuration = null
    // keep track of which components have finished
    blank500Components = [];
    blank500Components.push(text);
    
    blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function blank500RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blank500' ---
    // get current time
    t = blank500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blank500RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blank500' ---
    blank500Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('blank500.stopped', globalClock.getTime());
    if (blank500MaxDurationReached) {
        routineTimer.add(blank500MaxDuration);
    } else {
        routineTimer.add(-0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var familiarIntroMaxDurationReached;
var _familiarization_keyresp_allKeys;
var familiarIntroMaxDuration;
var familiarIntroComponents;
function familiarIntroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'familiarIntro' ---
    t = 0;
    familiarIntroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    familiarIntroMaxDurationReached = false;
    // update component parameters for each repeat
    familiarization_keyresp.keys = undefined;
    familiarization_keyresp.rt = undefined;
    _familiarization_keyresp_allKeys = [];
    psychoJS.experiment.addData('familiarIntro.started', globalClock.getTime());
    familiarIntroMaxDuration = null
    // keep track of which components have finished
    familiarIntroComponents = [];
    familiarIntroComponents.push(familiarization_intro);
    familiarIntroComponents.push(familiarization_keyresp);
    
    familiarIntroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function familiarIntroRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'familiarIntro' ---
    // get current time
    t = familiarIntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *familiarization_intro* updates
    if (t >= 0.0 && familiarization_intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      familiarization_intro.tStart = t;  // (not accounting for frame time here)
      familiarization_intro.frameNStart = frameN;  // exact frame index
      
      familiarization_intro.setAutoDraw(true);
    }
    
    
    // *familiarization_keyresp* updates
    if (t >= 0.0 && familiarization_keyresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      familiarization_keyresp.tStart = t;  // (not accounting for frame time here)
      familiarization_keyresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { familiarization_keyresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { familiarization_keyresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { familiarization_keyresp.clearEvents(); });
    }
    
    if (familiarization_keyresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = familiarization_keyresp.getKeys({keyList: ['return'], waitRelease: false});
      _familiarization_keyresp_allKeys = _familiarization_keyresp_allKeys.concat(theseKeys);
      if (_familiarization_keyresp_allKeys.length > 0) {
        familiarization_keyresp.keys = _familiarization_keyresp_allKeys[_familiarization_keyresp_allKeys.length - 1].name;  // just the last key pressed
        familiarization_keyresp.rt = _familiarization_keyresp_allKeys[_familiarization_keyresp_allKeys.length - 1].rt;
        familiarization_keyresp.duration = _familiarization_keyresp_allKeys[_familiarization_keyresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    familiarIntroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function familiarIntroRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'familiarIntro' ---
    familiarIntroComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('familiarIntro.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(familiarization_keyresp.corr, level);
    }
    psychoJS.experiment.addData('familiarization_keyresp.keys', familiarization_keyresp.keys);
    if (typeof familiarization_keyresp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('familiarization_keyresp.rt', familiarization_keyresp.rt);
        psychoJS.experiment.addData('familiarization_keyresp.duration', familiarization_keyresp.duration);
        routineTimer.reset();
        }
    
    familiarization_keyresp.stop();
    // the Routine "familiarIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var NamingIntroMaxDurationReached;
var _NamingInstruct_keyresp_allKeys;
var NamingIntroMaxDuration;
var NamingIntroComponents;
function NamingIntroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'NamingIntro' ---
    t = 0;
    NamingIntroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    NamingIntroMaxDurationReached = false;
    // update component parameters for each repeat
    NamingInstruct_keyresp.keys = undefined;
    NamingInstruct_keyresp.rt = undefined;
    _NamingInstruct_keyresp_allKeys = [];
    psychoJS.experiment.addData('NamingIntro.started', globalClock.getTime());
    NamingIntroMaxDuration = null
    // keep track of which components have finished
    NamingIntroComponents = [];
    NamingIntroComponents.push(NamingInstruct_text);
    NamingIntroComponents.push(NamingInstruct_keyresp);
    
    NamingIntroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function NamingIntroRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'NamingIntro' ---
    // get current time
    t = NamingIntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NamingInstruct_text* updates
    if (t >= 0.0 && NamingInstruct_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NamingInstruct_text.tStart = t;  // (not accounting for frame time here)
      NamingInstruct_text.frameNStart = frameN;  // exact frame index
      
      NamingInstruct_text.setAutoDraw(true);
    }
    
    
    // *NamingInstruct_keyresp* updates
    if (t >= 0.0 && NamingInstruct_keyresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NamingInstruct_keyresp.tStart = t;  // (not accounting for frame time here)
      NamingInstruct_keyresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { NamingInstruct_keyresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { NamingInstruct_keyresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { NamingInstruct_keyresp.clearEvents(); });
    }
    
    if (NamingInstruct_keyresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = NamingInstruct_keyresp.getKeys({keyList: ['return'], waitRelease: false});
      _NamingInstruct_keyresp_allKeys = _NamingInstruct_keyresp_allKeys.concat(theseKeys);
      if (_NamingInstruct_keyresp_allKeys.length > 0) {
        NamingInstruct_keyresp.keys = _NamingInstruct_keyresp_allKeys[_NamingInstruct_keyresp_allKeys.length - 1].name;  // just the last key pressed
        NamingInstruct_keyresp.rt = _NamingInstruct_keyresp_allKeys[_NamingInstruct_keyresp_allKeys.length - 1].rt;
        NamingInstruct_keyresp.duration = _NamingInstruct_keyresp_allKeys[_NamingInstruct_keyresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    NamingIntroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NamingIntroRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'NamingIntro' ---
    NamingIntroComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('NamingIntro.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(NamingInstruct_keyresp.corr, level);
    }
    psychoJS.experiment.addData('NamingInstruct_keyresp.keys', NamingInstruct_keyresp.keys);
    if (typeof NamingInstruct_keyresp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('NamingInstruct_keyresp.rt', NamingInstruct_keyresp.rt);
        psychoJS.experiment.addData('NamingInstruct_keyresp.duration', NamingInstruct_keyresp.duration);
        routineTimer.reset();
        }
    
    NamingInstruct_keyresp.stop();
    // the Routine "NamingIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practiceTrialInstructionsMaxDurationReached;
var _PTInstruct_keyresp_allKeys;
var practiceTrialInstructionsMaxDuration;
var practiceTrialInstructionsComponents;
function practiceTrialInstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practiceTrialInstructions' ---
    t = 0;
    practiceTrialInstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practiceTrialInstructionsMaxDurationReached = false;
    // update component parameters for each repeat
    PTInstruct_keyresp.keys = undefined;
    PTInstruct_keyresp.rt = undefined;
    _PTInstruct_keyresp_allKeys = [];
    psychoJS.experiment.addData('practiceTrialInstructions.started', globalClock.getTime());
    practiceTrialInstructionsMaxDuration = null
    // keep track of which components have finished
    practiceTrialInstructionsComponents = [];
    practiceTrialInstructionsComponents.push(PTInstruct_text);
    practiceTrialInstructionsComponents.push(PTInstruct_keyresp);
    
    practiceTrialInstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practiceTrialInstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practiceTrialInstructions' ---
    // get current time
    t = practiceTrialInstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *PTInstruct_text* updates
    if (t >= 0.0 && PTInstruct_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PTInstruct_text.tStart = t;  // (not accounting for frame time here)
      PTInstruct_text.frameNStart = frameN;  // exact frame index
      
      PTInstruct_text.setAutoDraw(true);
    }
    
    
    // *PTInstruct_keyresp* updates
    if (t >= 0.0 && PTInstruct_keyresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PTInstruct_keyresp.tStart = t;  // (not accounting for frame time here)
      PTInstruct_keyresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PTInstruct_keyresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PTInstruct_keyresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PTInstruct_keyresp.clearEvents(); });
    }
    
    if (PTInstruct_keyresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = PTInstruct_keyresp.getKeys({keyList: ['return'], waitRelease: false});
      _PTInstruct_keyresp_allKeys = _PTInstruct_keyresp_allKeys.concat(theseKeys);
      if (_PTInstruct_keyresp_allKeys.length > 0) {
        PTInstruct_keyresp.keys = _PTInstruct_keyresp_allKeys[_PTInstruct_keyresp_allKeys.length - 1].name;  // just the last key pressed
        PTInstruct_keyresp.rt = _PTInstruct_keyresp_allKeys[_PTInstruct_keyresp_allKeys.length - 1].rt;
        PTInstruct_keyresp.duration = _PTInstruct_keyresp_allKeys[_PTInstruct_keyresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practiceTrialInstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practiceTrialInstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practiceTrialInstructions' ---
    practiceTrialInstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practiceTrialInstructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(PTInstruct_keyresp.corr, level);
    }
    psychoJS.experiment.addData('PTInstruct_keyresp.keys', PTInstruct_keyresp.keys);
    if (typeof PTInstruct_keyresp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('PTInstruct_keyresp.rt', PTInstruct_keyresp.rt);
        psychoJS.experiment.addData('PTInstruct_keyresp.duration', PTInstruct_keyresp.duration);
        routineTimer.reset();
        }
    
    PTInstruct_keyresp.stop();
    // the Routine "practiceTrialInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var TrialInstructionsMaxDurationReached;
var _TrialInstruct_keyresp_allKeys;
var TrialInstructionsMaxDuration;
var TrialInstructionsComponents;
function TrialInstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TrialInstructions' ---
    t = 0;
    TrialInstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    TrialInstructionsMaxDurationReached = false;
    // update component parameters for each repeat
    TrialInstruct_keyresp.keys = undefined;
    TrialInstruct_keyresp.rt = undefined;
    _TrialInstruct_keyresp_allKeys = [];
    psychoJS.experiment.addData('TrialInstructions.started', globalClock.getTime());
    TrialInstructionsMaxDuration = null
    // keep track of which components have finished
    TrialInstructionsComponents = [];
    TrialInstructionsComponents.push(TrialInstruct_text);
    TrialInstructionsComponents.push(TrialInstruct_keyresp);
    
    TrialInstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function TrialInstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TrialInstructions' ---
    // get current time
    t = TrialInstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *TrialInstruct_text* updates
    if (t >= 0.0 && TrialInstruct_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialInstruct_text.tStart = t;  // (not accounting for frame time here)
      TrialInstruct_text.frameNStart = frameN;  // exact frame index
      
      TrialInstruct_text.setAutoDraw(true);
    }
    
    
    // *TrialInstruct_keyresp* updates
    if (t >= 0.0 && TrialInstruct_keyresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialInstruct_keyresp.tStart = t;  // (not accounting for frame time here)
      TrialInstruct_keyresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { TrialInstruct_keyresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { TrialInstruct_keyresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { TrialInstruct_keyresp.clearEvents(); });
    }
    
    if (TrialInstruct_keyresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = TrialInstruct_keyresp.getKeys({keyList: ['return'], waitRelease: false});
      _TrialInstruct_keyresp_allKeys = _TrialInstruct_keyresp_allKeys.concat(theseKeys);
      if (_TrialInstruct_keyresp_allKeys.length > 0) {
        TrialInstruct_keyresp.keys = _TrialInstruct_keyresp_allKeys[_TrialInstruct_keyresp_allKeys.length - 1].name;  // just the last key pressed
        TrialInstruct_keyresp.rt = _TrialInstruct_keyresp_allKeys[_TrialInstruct_keyresp_allKeys.length - 1].rt;
        TrialInstruct_keyresp.duration = _TrialInstruct_keyresp_allKeys[_TrialInstruct_keyresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TrialInstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TrialInstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TrialInstructions' ---
    TrialInstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('TrialInstructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(TrialInstruct_keyresp.corr, level);
    }
    psychoJS.experiment.addData('TrialInstruct_keyresp.keys', TrialInstruct_keyresp.keys);
    if (typeof TrialInstruct_keyresp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('TrialInstruct_keyresp.rt', TrialInstruct_keyresp.rt);
        psychoJS.experiment.addData('TrialInstruct_keyresp.duration', TrialInstruct_keyresp.duration);
        routineTimer.reset();
        }
    
    TrialInstruct_keyresp.stop();
    // the Routine "TrialInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Trial_1;
function Trial_1LoopBegin(Trial_1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Trial_1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'exp_items_s1.csv',
      seed: undefined, name: 'Trial_1'
    });
    psychoJS.experiment.addLoop(Trial_1); // add the loop to the experiment
    currentLoop = Trial_1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Trial_1.forEach(function() {
      snapshot = Trial_1.getSnapshot();
    
      Trial_1LoopScheduler.add(importConditions(snapshot));
      Trial_1LoopScheduler.add(blank500RoutineBegin(snapshot));
      Trial_1LoopScheduler.add(blank500RoutineEachFrame());
      Trial_1LoopScheduler.add(blank500RoutineEnd(snapshot));
      Trial_1LoopScheduler.add(Trial_Set_1RoutineBegin(snapshot));
      Trial_1LoopScheduler.add(Trial_Set_1RoutineEachFrame());
      Trial_1LoopScheduler.add(Trial_Set_1RoutineEnd(snapshot));
      Trial_1LoopScheduler.add(Trial_1LoopEndIteration(Trial_1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Trial_1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Trial_1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function Trial_1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var Trial_2;
function Trial_2LoopBegin(Trial_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Trial_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'exp_items_s2.csv',
      seed: undefined, name: 'Trial_2'
    });
    psychoJS.experiment.addLoop(Trial_2); // add the loop to the experiment
    currentLoop = Trial_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Trial_2.forEach(function() {
      snapshot = Trial_2.getSnapshot();
    
      Trial_2LoopScheduler.add(importConditions(snapshot));
      Trial_2LoopScheduler.add(blank500RoutineBegin(snapshot));
      Trial_2LoopScheduler.add(blank500RoutineEachFrame());
      Trial_2LoopScheduler.add(blank500RoutineEnd(snapshot));
      Trial_2LoopScheduler.add(Trial_Set_2RoutineBegin(snapshot));
      Trial_2LoopScheduler.add(Trial_Set_2RoutineEachFrame());
      Trial_2LoopScheduler.add(Trial_Set_2RoutineEnd(snapshot));
      Trial_2LoopScheduler.add(Trial_2LoopEndIteration(Trial_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Trial_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Trial_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function Trial_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var Trial_3;
function Trial_3LoopBegin(Trial_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Trial_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'exp_items_s3.csv',
      seed: undefined, name: 'Trial_3'
    });
    psychoJS.experiment.addLoop(Trial_3); // add the loop to the experiment
    currentLoop = Trial_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Trial_3.forEach(function() {
      snapshot = Trial_3.getSnapshot();
    
      Trial_3LoopScheduler.add(importConditions(snapshot));
      Trial_3LoopScheduler.add(blank500RoutineBegin(snapshot));
      Trial_3LoopScheduler.add(blank500RoutineEachFrame());
      Trial_3LoopScheduler.add(blank500RoutineEnd(snapshot));
      Trial_3LoopScheduler.add(Trial_Set_3RoutineBegin(snapshot));
      Trial_3LoopScheduler.add(Trial_Set_3RoutineEachFrame());
      Trial_3LoopScheduler.add(Trial_Set_3RoutineEnd(snapshot));
      Trial_3LoopScheduler.add(Trial_3LoopEndIteration(Trial_3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Trial_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Trial_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function Trial_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var Trial_4;
function Trial_4LoopBegin(Trial_4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Trial_4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'exp_items_s4.csv',
      seed: undefined, name: 'Trial_4'
    });
    psychoJS.experiment.addLoop(Trial_4); // add the loop to the experiment
    currentLoop = Trial_4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Trial_4.forEach(function() {
      snapshot = Trial_4.getSnapshot();
    
      Trial_4LoopScheduler.add(importConditions(snapshot));
      Trial_4LoopScheduler.add(blank500RoutineBegin(snapshot));
      Trial_4LoopScheduler.add(blank500RoutineEachFrame());
      Trial_4LoopScheduler.add(blank500RoutineEnd(snapshot));
      Trial_4LoopScheduler.add(Trial_Set_4RoutineBegin(snapshot));
      Trial_4LoopScheduler.add(Trial_Set_4RoutineEachFrame());
      Trial_4LoopScheduler.add(Trial_Set_4RoutineEnd(snapshot));
      Trial_4LoopScheduler.add(Trial_4LoopEndIteration(Trial_4LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Trial_4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Trial_4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function Trial_4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var Trial_Set_1MaxDurationReached;
var _Enter_Response_Set_1_allKeys;
var Trial_Set_1MaxDuration;
var Trial_Set_1Components;
function Trial_Set_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Trial_Set_1' ---
    t = 0;
    Trial_Set_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Trial_Set_1MaxDurationReached = false;
    // update component parameters for each repeat
    image_2_set_1.setImage(image_2);
    image_1_set_1.setImage(image);
    Enter_Text_Set_1.setText('Press Enter When Ready');
    Enter_Response_Set_1.keys = undefined;
    Enter_Response_Set_1.rt = undefined;
    _Enter_Response_Set_1_allKeys = [];
    psychoJS.experiment.addData('Trial_Set_1.started', globalClock.getTime());
    Trial_Set_1MaxDuration = null
    // keep track of which components have finished
    Trial_Set_1Components = [];
    Trial_Set_1Components.push(Fixation_Set_1);
    Trial_Set_1Components.push(image_2_set_1);
    Trial_Set_1Components.push(image_1_set_1);
    Trial_Set_1Components.push(Recording_Circle_Set_1);
    Trial_Set_1Components.push(Enter_Text_Set_1);
    Trial_Set_1Components.push(Enter_Response_Set_1);
    
    Trial_Set_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Trial_Set_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Trial_Set_1' ---
    // get current time
    t = Trial_Set_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Fixation_Set_1* updates
    if (t >= 0.0 && Fixation_Set_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation_Set_1.tStart = t;  // (not accounting for frame time here)
      Fixation_Set_1.frameNStart = frameN;  // exact frame index
      
      Fixation_Set_1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Fixation_Set_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fixation_Set_1.setAutoDraw(false);
    }
    
    
    // *image_2_set_1* updates
    if (t >= 0.45 && image_2_set_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2_set_1.tStart = t;  // (not accounting for frame time here)
      image_2_set_1.frameNStart = frameN;  // exact frame index
      
      image_2_set_1.setAutoDraw(true);
    }
    
    
    // *image_1_set_1* updates
    if (t >= 0.3 && image_1_set_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_1_set_1.tStart = t;  // (not accounting for frame time here)
      image_1_set_1.frameNStart = frameN;  // exact frame index
      
      image_1_set_1.setAutoDraw(true);
    }
    
    frameRemains = 0.3 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_1_set_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_1_set_1.setAutoDraw(false);
    }
    
    
    // *Recording_Circle_Set_1* updates
    if (t >= 0.3 && Recording_Circle_Set_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Recording_Circle_Set_1.tStart = t;  // (not accounting for frame time here)
      Recording_Circle_Set_1.frameNStart = frameN;  // exact frame index
      
      Recording_Circle_Set_1.setAutoDraw(true);
    }
    
    frameRemains = 0.3 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Recording_Circle_Set_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Recording_Circle_Set_1.setAutoDraw(false);
    }
    
    
    // *Enter_Text_Set_1* updates
    if (t >= 4.3 && Enter_Text_Set_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Enter_Text_Set_1.tStart = t;  // (not accounting for frame time here)
      Enter_Text_Set_1.frameNStart = frameN;  // exact frame index
      
      Enter_Text_Set_1.setAutoDraw(true);
    }
    
    
    // *Enter_Response_Set_1* updates
    if (t >= 0.3 && Enter_Response_Set_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Enter_Response_Set_1.tStart = t;  // (not accounting for frame time here)
      Enter_Response_Set_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_1.clearEvents(); });
    }
    
    if (Enter_Response_Set_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = Enter_Response_Set_1.getKeys({keyList: ['return'], waitRelease: false});
      _Enter_Response_Set_1_allKeys = _Enter_Response_Set_1_allKeys.concat(theseKeys);
      if (_Enter_Response_Set_1_allKeys.length > 0) {
        Enter_Response_Set_1.keys = _Enter_Response_Set_1_allKeys[_Enter_Response_Set_1_allKeys.length - 1].name;  // just the last key pressed
        Enter_Response_Set_1.rt = _Enter_Response_Set_1_allKeys[_Enter_Response_Set_1_allKeys.length - 1].rt;
        Enter_Response_Set_1.duration = _Enter_Response_Set_1_allKeys[_Enter_Response_Set_1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Trial_Set_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Trial_Set_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Trial_Set_1' ---
    Trial_Set_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Trial_Set_1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Enter_Response_Set_1.corr, level);
    }
    psychoJS.experiment.addData('Enter_Response_Set_1.keys', Enter_Response_Set_1.keys);
    if (typeof Enter_Response_Set_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Enter_Response_Set_1.rt', Enter_Response_Set_1.rt);
        psychoJS.experiment.addData('Enter_Response_Set_1.duration', Enter_Response_Set_1.duration);
        routineTimer.reset();
        }
    
    Enter_Response_Set_1.stop();
    // the Routine "Trial_Set_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var betweentrialbreakMaxDurationReached;
var _key_resp_allKeys;
var betweentrialbreakMaxDuration;
var betweentrialbreakComponents;
function betweentrialbreakRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'betweentrialbreak' ---
    t = 0;
    betweentrialbreakClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    betweentrialbreakMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('betweentrialbreak.started', globalClock.getTime());
    betweentrialbreakMaxDuration = null
    // keep track of which components have finished
    betweentrialbreakComponents = [];
    betweentrialbreakComponents.push(text_6);
    betweentrialbreakComponents.push(key_resp);
    betweentrialbreakComponents.push(ten);
    betweentrialbreakComponents.push(nine);
    betweentrialbreakComponents.push(eight);
    betweentrialbreakComponents.push(seven);
    betweentrialbreakComponents.push(six);
    betweentrialbreakComponents.push(five);
    betweentrialbreakComponents.push(four);
    betweentrialbreakComponents.push(three);
    betweentrialbreakComponents.push(two);
    betweentrialbreakComponents.push(one);
    betweentrialbreakComponents.push(text_16end);
    
    betweentrialbreakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function betweentrialbreakRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'betweentrialbreak' ---
    // get current time
    t = betweentrialbreakClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_6.setAutoDraw(false);
    }
    
    
    // *key_resp* updates
    if (t >= 0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['return'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *ten* updates
    if (t >= 50 && ten.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ten.tStart = t;  // (not accounting for frame time here)
      ten.frameNStart = frameN;  // exact frame index
      
      ten.setAutoDraw(true);
    }
    
    frameRemains = 50 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (ten.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ten.setAutoDraw(false);
    }
    
    
    // *nine* updates
    if (t >= 51 && nine.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nine.tStart = t;  // (not accounting for frame time here)
      nine.frameNStart = frameN;  // exact frame index
      
      nine.setAutoDraw(true);
    }
    
    frameRemains = 51 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (nine.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      nine.setAutoDraw(false);
    }
    
    
    // *eight* updates
    if (t >= 52 && eight.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eight.tStart = t;  // (not accounting for frame time here)
      eight.frameNStart = frameN;  // exact frame index
      
      eight.setAutoDraw(true);
    }
    
    frameRemains = 52 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (eight.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      eight.setAutoDraw(false);
    }
    
    
    // *seven* updates
    if (t >= 53 && seven.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      seven.tStart = t;  // (not accounting for frame time here)
      seven.frameNStart = frameN;  // exact frame index
      
      seven.setAutoDraw(true);
    }
    
    frameRemains = 53 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (seven.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      seven.setAutoDraw(false);
    }
    
    
    // *six* updates
    if (t >= 54 && six.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      six.tStart = t;  // (not accounting for frame time here)
      six.frameNStart = frameN;  // exact frame index
      
      six.setAutoDraw(true);
    }
    
    frameRemains = 54 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (six.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      six.setAutoDraw(false);
    }
    
    
    // *five* updates
    if (t >= 55 && five.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five.tStart = t;  // (not accounting for frame time here)
      five.frameNStart = frameN;  // exact frame index
      
      five.setAutoDraw(true);
    }
    
    frameRemains = 55 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (five.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      five.setAutoDraw(false);
    }
    
    
    // *four* updates
    if (t >= 56 && four.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      four.tStart = t;  // (not accounting for frame time here)
      four.frameNStart = frameN;  // exact frame index
      
      four.setAutoDraw(true);
    }
    
    frameRemains = 56 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (four.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      four.setAutoDraw(false);
    }
    
    
    // *three* updates
    if (t >= 57 && three.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      three.tStart = t;  // (not accounting for frame time here)
      three.frameNStart = frameN;  // exact frame index
      
      three.setAutoDraw(true);
    }
    
    frameRemains = 57 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (three.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      three.setAutoDraw(false);
    }
    
    
    // *two* updates
    if (t >= 58 && two.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      two.tStart = t;  // (not accounting for frame time here)
      two.frameNStart = frameN;  // exact frame index
      
      two.setAutoDraw(true);
    }
    
    frameRemains = 58 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (two.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      two.setAutoDraw(false);
    }
    
    
    // *one* updates
    if (t >= 59 && one.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      one.tStart = t;  // (not accounting for frame time here)
      one.frameNStart = frameN;  // exact frame index
      
      one.setAutoDraw(true);
    }
    
    frameRemains = 59 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (one.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      one.setAutoDraw(false);
    }
    
    
    // *text_16end* updates
    if (t >= 60 && text_16end.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_16end.tStart = t;  // (not accounting for frame time here)
      text_16end.frameNStart = frameN;  // exact frame index
      
      text_16end.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    betweentrialbreakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function betweentrialbreakRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'betweentrialbreak' ---
    betweentrialbreakComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('betweentrialbreak.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "betweentrialbreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var NewSetBeginMaxDurationReached;
var NewSetBeginMaxDuration;
var NewSetBeginComponents;
function NewSetBeginRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'NewSetBegin' ---
    t = 0;
    NewSetBeginClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    NewSetBeginMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('NewSetBegin.started', globalClock.getTime());
    NewSetBeginMaxDuration = null
    // keep track of which components have finished
    NewSetBeginComponents = [];
    NewSetBeginComponents.push(text_NewSet);
    
    NewSetBeginComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function NewSetBeginRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'NewSetBegin' ---
    // get current time
    t = NewSetBeginClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_NewSet* updates
    if (t >= 0.0 && text_NewSet.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_NewSet.tStart = t;  // (not accounting for frame time here)
      text_NewSet.frameNStart = frameN;  // exact frame index
      
      text_NewSet.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_NewSet.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_NewSet.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    NewSetBeginComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NewSetBeginRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'NewSetBegin' ---
    NewSetBeginComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('NewSetBegin.stopped', globalClock.getTime());
    if (NewSetBeginMaxDurationReached) {
        routineTimer.add(NewSetBeginMaxDuration);
    } else {
        routineTimer.add(-1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Trial_Set_2MaxDurationReached;
var _Enter_Response_Set_2_allKeys;
var Trial_Set_2MaxDuration;
var Trial_Set_2Components;
function Trial_Set_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Trial_Set_2' ---
    t = 0;
    Trial_Set_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Trial_Set_2MaxDurationReached = false;
    // update component parameters for each repeat
    image_2_set_2.setImage(image_2);
    image_1_set_2.setImage(image);
    Enter_Text_Set_2.setText('Press Enter When Ready');
    Enter_Response_Set_2.keys = undefined;
    Enter_Response_Set_2.rt = undefined;
    _Enter_Response_Set_2_allKeys = [];
    psychoJS.experiment.addData('Trial_Set_2.started', globalClock.getTime());
    Trial_Set_2MaxDuration = null
    // keep track of which components have finished
    Trial_Set_2Components = [];
    Trial_Set_2Components.push(Fixation_Set_2);
    Trial_Set_2Components.push(image_2_set_2);
    Trial_Set_2Components.push(image_1_set_2);
    Trial_Set_2Components.push(Recording_Circle_Set_2);
    Trial_Set_2Components.push(Enter_Text_Set_2);
    Trial_Set_2Components.push(Enter_Response_Set_2);
    
    Trial_Set_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Trial_Set_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Trial_Set_2' ---
    // get current time
    t = Trial_Set_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Fixation_Set_2* updates
    if (t >= 0.0 && Fixation_Set_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation_Set_2.tStart = t;  // (not accounting for frame time here)
      Fixation_Set_2.frameNStart = frameN;  // exact frame index
      
      Fixation_Set_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Fixation_Set_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fixation_Set_2.setAutoDraw(false);
    }
    
    
    // *image_2_set_2* updates
    if (t >= 0.45 && image_2_set_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2_set_2.tStart = t;  // (not accounting for frame time here)
      image_2_set_2.frameNStart = frameN;  // exact frame index
      
      image_2_set_2.setAutoDraw(true);
    }
    
    
    // *image_1_set_2* updates
    if (t >= 0.3 && image_1_set_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_1_set_2.tStart = t;  // (not accounting for frame time here)
      image_1_set_2.frameNStart = frameN;  // exact frame index
      
      image_1_set_2.setAutoDraw(true);
    }
    
    frameRemains = 0.3 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_1_set_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_1_set_2.setAutoDraw(false);
    }
    
    
    // *Recording_Circle_Set_2* updates
    if (t >= 0.3 && Recording_Circle_Set_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Recording_Circle_Set_2.tStart = t;  // (not accounting for frame time here)
      Recording_Circle_Set_2.frameNStart = frameN;  // exact frame index
      
      Recording_Circle_Set_2.setAutoDraw(true);
    }
    
    frameRemains = 0.3 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Recording_Circle_Set_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Recording_Circle_Set_2.setAutoDraw(false);
    }
    
    
    // *Enter_Text_Set_2* updates
    if (t >= 4.3 && Enter_Text_Set_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Enter_Text_Set_2.tStart = t;  // (not accounting for frame time here)
      Enter_Text_Set_2.frameNStart = frameN;  // exact frame index
      
      Enter_Text_Set_2.setAutoDraw(true);
    }
    
    
    // *Enter_Response_Set_2* updates
    if (t >= 0.3 && Enter_Response_Set_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Enter_Response_Set_2.tStart = t;  // (not accounting for frame time here)
      Enter_Response_Set_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_2.clearEvents(); });
    }
    
    if (Enter_Response_Set_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = Enter_Response_Set_2.getKeys({keyList: ['return'], waitRelease: false});
      _Enter_Response_Set_2_allKeys = _Enter_Response_Set_2_allKeys.concat(theseKeys);
      if (_Enter_Response_Set_2_allKeys.length > 0) {
        Enter_Response_Set_2.keys = _Enter_Response_Set_2_allKeys[_Enter_Response_Set_2_allKeys.length - 1].name;  // just the last key pressed
        Enter_Response_Set_2.rt = _Enter_Response_Set_2_allKeys[_Enter_Response_Set_2_allKeys.length - 1].rt;
        Enter_Response_Set_2.duration = _Enter_Response_Set_2_allKeys[_Enter_Response_Set_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Trial_Set_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Trial_Set_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Trial_Set_2' ---
    Trial_Set_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Trial_Set_2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Enter_Response_Set_2.corr, level);
    }
    psychoJS.experiment.addData('Enter_Response_Set_2.keys', Enter_Response_Set_2.keys);
    if (typeof Enter_Response_Set_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Enter_Response_Set_2.rt', Enter_Response_Set_2.rt);
        psychoJS.experiment.addData('Enter_Response_Set_2.duration', Enter_Response_Set_2.duration);
        routineTimer.reset();
        }
    
    Enter_Response_Set_2.stop();
    // the Routine "Trial_Set_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Trial_Set_3MaxDurationReached;
var _Enter_Response_Set_3_allKeys;
var Trial_Set_3MaxDuration;
var Trial_Set_3Components;
function Trial_Set_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Trial_Set_3' ---
    t = 0;
    Trial_Set_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Trial_Set_3MaxDurationReached = false;
    // update component parameters for each repeat
    image_2_set_3.setImage(image_2);
    image_1_set_3.setImage(image_2);
    Enter_Text_Set_3.setText('Press Enter When Ready');
    Enter_Response_Set_3.keys = undefined;
    Enter_Response_Set_3.rt = undefined;
    _Enter_Response_Set_3_allKeys = [];
    psychoJS.experiment.addData('Trial_Set_3.started', globalClock.getTime());
    Trial_Set_3MaxDuration = null
    // keep track of which components have finished
    Trial_Set_3Components = [];
    Trial_Set_3Components.push(Fixation_Set_3);
    Trial_Set_3Components.push(image_2_set_3);
    Trial_Set_3Components.push(image_1_set_3);
    Trial_Set_3Components.push(Recording_Circle_Set_3);
    Trial_Set_3Components.push(Enter_Text_Set_3);
    Trial_Set_3Components.push(Enter_Response_Set_3);
    
    Trial_Set_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Trial_Set_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Trial_Set_3' ---
    // get current time
    t = Trial_Set_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Fixation_Set_3* updates
    if (t >= 0.0 && Fixation_Set_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation_Set_3.tStart = t;  // (not accounting for frame time here)
      Fixation_Set_3.frameNStart = frameN;  // exact frame index
      
      Fixation_Set_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Fixation_Set_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fixation_Set_3.setAutoDraw(false);
    }
    
    
    // *image_2_set_3* updates
    if (t >= 0.45 && image_2_set_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2_set_3.tStart = t;  // (not accounting for frame time here)
      image_2_set_3.frameNStart = frameN;  // exact frame index
      
      image_2_set_3.setAutoDraw(true);
    }
    
    
    // *image_1_set_3* updates
    if (t >= 0.3 && image_1_set_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_1_set_3.tStart = t;  // (not accounting for frame time here)
      image_1_set_3.frameNStart = frameN;  // exact frame index
      
      image_1_set_3.setAutoDraw(true);
    }
    
    frameRemains = 0.3 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_1_set_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_1_set_3.setAutoDraw(false);
    }
    
    
    // *Recording_Circle_Set_3* updates
    if (t >= 0.3 && Recording_Circle_Set_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Recording_Circle_Set_3.tStart = t;  // (not accounting for frame time here)
      Recording_Circle_Set_3.frameNStart = frameN;  // exact frame index
      
      Recording_Circle_Set_3.setAutoDraw(true);
    }
    
    frameRemains = 0.3 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Recording_Circle_Set_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Recording_Circle_Set_3.setAutoDraw(false);
    }
    
    
    // *Enter_Text_Set_3* updates
    if (t >= 4.3 && Enter_Text_Set_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Enter_Text_Set_3.tStart = t;  // (not accounting for frame time here)
      Enter_Text_Set_3.frameNStart = frameN;  // exact frame index
      
      Enter_Text_Set_3.setAutoDraw(true);
    }
    
    
    // *Enter_Response_Set_3* updates
    if (t >= 0.3 && Enter_Response_Set_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Enter_Response_Set_3.tStart = t;  // (not accounting for frame time here)
      Enter_Response_Set_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_3.clearEvents(); });
    }
    
    if (Enter_Response_Set_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = Enter_Response_Set_3.getKeys({keyList: ['return'], waitRelease: false});
      _Enter_Response_Set_3_allKeys = _Enter_Response_Set_3_allKeys.concat(theseKeys);
      if (_Enter_Response_Set_3_allKeys.length > 0) {
        Enter_Response_Set_3.keys = _Enter_Response_Set_3_allKeys[_Enter_Response_Set_3_allKeys.length - 1].name;  // just the last key pressed
        Enter_Response_Set_3.rt = _Enter_Response_Set_3_allKeys[_Enter_Response_Set_3_allKeys.length - 1].rt;
        Enter_Response_Set_3.duration = _Enter_Response_Set_3_allKeys[_Enter_Response_Set_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Trial_Set_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Trial_Set_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Trial_Set_3' ---
    Trial_Set_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Trial_Set_3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Enter_Response_Set_3.corr, level);
    }
    psychoJS.experiment.addData('Enter_Response_Set_3.keys', Enter_Response_Set_3.keys);
    if (typeof Enter_Response_Set_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Enter_Response_Set_3.rt', Enter_Response_Set_3.rt);
        psychoJS.experiment.addData('Enter_Response_Set_3.duration', Enter_Response_Set_3.duration);
        routineTimer.reset();
        }
    
    Enter_Response_Set_3.stop();
    // the Routine "Trial_Set_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Trial_Set_4MaxDurationReached;
var _Enter_Response_Set_4_allKeys;
var Trial_Set_4MaxDuration;
var Trial_Set_4Components;
function Trial_Set_4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Trial_Set_4' ---
    t = 0;
    Trial_Set_4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Trial_Set_4MaxDurationReached = false;
    // update component parameters for each repeat
    image_2_set_4.setImage(image_2);
    image_1_set_4.setImage(image);
    Enter_Text_Set_4.setText('Press Enter When Ready');
    Enter_Response_Set_4.keys = undefined;
    Enter_Response_Set_4.rt = undefined;
    _Enter_Response_Set_4_allKeys = [];
    psychoJS.experiment.addData('Trial_Set_4.started', globalClock.getTime());
    Trial_Set_4MaxDuration = null
    // keep track of which components have finished
    Trial_Set_4Components = [];
    Trial_Set_4Components.push(Fixation_Set_4);
    Trial_Set_4Components.push(image_2_set_4);
    Trial_Set_4Components.push(image_1_set_4);
    Trial_Set_4Components.push(Recording_Circle_Set_4);
    Trial_Set_4Components.push(Enter_Text_Set_4);
    Trial_Set_4Components.push(Enter_Response_Set_4);
    
    Trial_Set_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Trial_Set_4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Trial_Set_4' ---
    // get current time
    t = Trial_Set_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Fixation_Set_4* updates
    if (t >= 0.0 && Fixation_Set_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fixation_Set_4.tStart = t;  // (not accounting for frame time here)
      Fixation_Set_4.frameNStart = frameN;  // exact frame index
      
      Fixation_Set_4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Fixation_Set_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fixation_Set_4.setAutoDraw(false);
    }
    
    
    // *image_2_set_4* updates
    if (t >= 0.45 && image_2_set_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2_set_4.tStart = t;  // (not accounting for frame time here)
      image_2_set_4.frameNStart = frameN;  // exact frame index
      
      image_2_set_4.setAutoDraw(true);
    }
    
    
    // *image_1_set_4* updates
    if (t >= 0.3 && image_1_set_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_1_set_4.tStart = t;  // (not accounting for frame time here)
      image_1_set_4.frameNStart = frameN;  // exact frame index
      
      image_1_set_4.setAutoDraw(true);
    }
    
    frameRemains = 0.3 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_1_set_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_1_set_4.setAutoDraw(false);
    }
    
    
    // *Recording_Circle_Set_4* updates
    if (t >= 0.3 && Recording_Circle_Set_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Recording_Circle_Set_4.tStart = t;  // (not accounting for frame time here)
      Recording_Circle_Set_4.frameNStart = frameN;  // exact frame index
      
      Recording_Circle_Set_4.setAutoDraw(true);
    }
    
    frameRemains = 0.3 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Recording_Circle_Set_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Recording_Circle_Set_4.setAutoDraw(false);
    }
    
    
    // *Enter_Text_Set_4* updates
    if (t >= 4.3 && Enter_Text_Set_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Enter_Text_Set_4.tStart = t;  // (not accounting for frame time here)
      Enter_Text_Set_4.frameNStart = frameN;  // exact frame index
      
      Enter_Text_Set_4.setAutoDraw(true);
    }
    
    
    // *Enter_Response_Set_4* updates
    if (t >= 4.3 && Enter_Response_Set_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Enter_Response_Set_4.tStart = t;  // (not accounting for frame time here)
      Enter_Response_Set_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Enter_Response_Set_4.clearEvents(); });
    }
    
    if (Enter_Response_Set_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = Enter_Response_Set_4.getKeys({keyList: ['return'], waitRelease: false});
      _Enter_Response_Set_4_allKeys = _Enter_Response_Set_4_allKeys.concat(theseKeys);
      if (_Enter_Response_Set_4_allKeys.length > 0) {
        Enter_Response_Set_4.keys = _Enter_Response_Set_4_allKeys[_Enter_Response_Set_4_allKeys.length - 1].name;  // just the last key pressed
        Enter_Response_Set_4.rt = _Enter_Response_Set_4_allKeys[_Enter_Response_Set_4_allKeys.length - 1].rt;
        Enter_Response_Set_4.duration = _Enter_Response_Set_4_allKeys[_Enter_Response_Set_4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Trial_Set_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Trial_Set_4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Trial_Set_4' ---
    Trial_Set_4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Trial_Set_4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Enter_Response_Set_4.corr, level);
    }
    psychoJS.experiment.addData('Enter_Response_Set_4.keys', Enter_Response_Set_4.keys);
    if (typeof Enter_Response_Set_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Enter_Response_Set_4.rt', Enter_Response_Set_4.rt);
        psychoJS.experiment.addData('Enter_Response_Set_4.duration', Enter_Response_Set_4.duration);
        routineTimer.reset();
        }
    
    Enter_Response_Set_4.stop();
    // the Routine "Trial_Set_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var goodbyeMaxDurationReached;
var _key_resp_2_allKeys;
var goodbyeMaxDuration;
var goodbyeComponents;
function goodbyeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'goodbye' ---
    t = 0;
    goodbyeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    goodbyeMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    psychoJS.experiment.addData('goodbye.started', globalClock.getTime());
    goodbyeMaxDuration = null
    // keep track of which components have finished
    goodbyeComponents = [];
    goodbyeComponents.push(textGoodbye);
    goodbyeComponents.push(key_resp_2);
    
    goodbyeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function goodbyeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'goodbye' ---
    // get current time
    t = goodbyeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textGoodbye* updates
    if (t >= 0.0 && textGoodbye.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textGoodbye.tStart = t;  // (not accounting for frame time here)
      textGoodbye.frameNStart = frameN;  // exact frame index
      
      textGoodbye.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textGoodbye.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textGoodbye.setAutoDraw(false);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_2.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['return'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    goodbyeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function goodbyeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'goodbye' ---
    goodbyeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('goodbye.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    if (goodbyeMaxDurationReached) {
        routineTimer.add(goodbyeMaxDuration);
    } else {
        routineTimer.add(-10.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
